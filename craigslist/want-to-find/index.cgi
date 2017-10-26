#!/usr/local/bin/perl5 -s

###############
##<-- 2k10 -->##
###############
###############
##<-- 2k13 -->##
###############
###############
##<-- 2k17 -->##
###############

$|=1;

use LWP::Simple;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use HTML::SimpleLinkExtor;
use HTML::TokeParser;
use HTML::ResolveLink;
use Text::Autoformat;
autoformat;

require("../q.pl");

$ms = $FORM{'query'};


	$hssel = '';
	if ($FORM{'hasPic'} eq "1") { $hssel = 'checked'; }

	#$rsssel = '';
	#if ($FORM{'format'} eq "rss") { $rsssel = 'checked'; }

	$shoth = '';
	$showThumbs = '0';
	if ($FORM{'showThumbs'} eq "1") { $shoth = 'checked'; $showThumbs = '1'; }

	##-- set defaults
	$cualstate = 'California';
	$location = 'losangeles';

	if ($FORM{'state'} ne '') { $cualstate = $FORM{'state'}; }
	if ($FORM{'loc'}) { $location = $FORM{'loc'}; }

	if ($cualstate ne '') {
		$usaListLocations = `cat ../craigslistLocations-US.dat`;
		@clStates = split(/\n\n/,$usaListLocations);

		$iveSeenState = '';
		foreach $clstate (@clStates) {
			@estosStateLocations = split(/\n/,$clstate);
			
			$currentState = '';
			foreach $thisStateLocations (@estosStateLocations) {
				@esteStateLocationOne = split(/-/,$thisStateLocations);
				if ($iveSeenState !~ $esteStateLocationOne[1]) {
					$iveSeenState .= $esteStateLocationOne[1];
					$currentState = $esteStateLocationOne[1];
					$stateSelected = '';
					if ($cualstate eq $esteStateLocationOne[1]) { $stateSelected = 'selected'; }
					push(@clEstados,"<option value='$esteStateLocationOne[1]' $stateSelected>$esteStateLocationOne[1]</option>");
				}
				$thisStateLocations =~ s/^\s*(\S*(?:\s+\S+)*)\s*$/$1/;
				$thisStateLocations =~ s/\n//gi;
				$thisStateLocations =~ s/\r//gi;
				if ($cualstate eq $currentState) {
					if ($thisStateLocations ne '') {
						push(@clEstadoLocations,"$thisStateLocations");
					}
				}
			}
		}
	}
	$todosCLstates = join "\n", @clEstados;

	$multicit = '';
	$multiCities = '0';
	$paginator = '';
	if ($FORM{'multipleAreas'} eq "1") { 
		$multicit = 'checked'; 
		$multiCities = '1'; 
		#-- hide .paginator, prev/next controls
		$paginator = 'display:none;';
	}

	if ($FORM{'SLS'} ne "" && $FORM{'multipleAreas'} eq "1") {
		$multiCities = '1'; 
	}

	$stAsel = 'checked'; $stTsel = '';
	if ($FORM{'srchType'} eq "T") { $stTsel = 'checked'; $stAsel = ''; }

	$catAbb = 'sss';
	if ($FORM{'catAbb'}) { $catAbb = $FORM{'catAbb'}; }

	#- query=2009&srchType=A&minAsk=1000&maxAsk=3500&hasPic=1&showThumbs=1&multipleCities=1
	#- srchType = A [entire post] | T [title only]
	#- hasPic [pass this param only if true]
	#- showThumbs [never pass, only a local param]
	#- catAbb=cto
	#- allSelectedStateCities=1

	#- added 2013 pagination support
	#- s=100


	$craigsList = `cat ./craigslist.dat`;
	$craigsListSort = `cat ../craigslistSort.dat`;
	@clList = split(/\n/,$craigsList);
	@clSort = split(/\n/,$craigsListSort);
	foreach $cll (@clList) {
		$cll =~ s/<\/option>//gi; $cll =~ s/>//gi; $cll =~ s/\r//gi;
		($cll,$value,$name) = split(/"/,$cll);
		$isSelected = '';
		if ($catAbb eq $value) { $isSelected = 'selected'; }
		push(@TheCL,"<option value='$value' $isSelected>$name</option>");
	}
	$craigsList = join "\n", @TheCL;

	##-- push the blank option for dynamic selection upon change of state, should be first option
	push(@TheCLLocations,"<option value=''></option>");
	$properStateLocationSelected = 0;
	$allChecked = 0;
	##--all or multiple
	$AllMulti = 'Selected';
	$Locations = 'Location';
	foreach $clloc (@clEstadoLocations) {
		($country,$state,$url,$name) = split(/-/,$clloc);
		$myShortLocation = $url;
		$http = 'http://';
		##-- common url attributes
		$myShortLocation =~ s/$http//gi;
		$myShortLocation =~ s/\.craigslist\.org//gi;
		##-- remove spaces
		$isSelected = '';
		if ($location eq "$myShortLocation") {
			$isSelected = 'selected';
			$properStateLocationSelected++;
		}

		@myTSLs = split(/ /,$name);
		@newTSL = '';
		foreach $unTSL (@myTSLs) {
			$thisTSL = $unTSL;
			$thisTSL = autoformat $thisTSL, { case => 'title' };
			chomp($thisTSL);
			$thisTSL =~ s/\n//gi;
			push(@newTSL,$thisTSL);
		}
		$name = join " ", @newTSL;

		##-- select list options
		push(@TheCLLocations,"<option value='$myShortLocation' $isSelected>$name</option>");

		push(@ShortCLlocations,"$myShortLocation");

		##-- checkboxes
		$LocationChecked = '';
		if ($FORM{'SLS'} =~ "$myShortLocation" && $FORM{'multipleAreas'} eq "1") { $allChecked++; $LocationChecked = 'checked'; }
		push(@TheCLLocationCheckboxes,"<span class='activeLocationData'><span><input type='checkbox' name='SLS' value='$myShortLocation' id='$myShortLocation' onChange='javascript:locChange(this);' $LocationChecked><label for='$myShortLocation'>$name</label></span></span>");
		
		##-- hash the location names by their relative values
		$theLocationNames{$myShortLocation}="$name";
	}
	##--all or multiple
	if ($allChecked == 0) { $AllMulti = 'All'; $Locations = 'Locations'; }
	elsif ($allChecked >= 2) { $Locations = 'Locations'; }

	##-- if changing state, meaning location must be improper, force search on 1st available location of state
	if ($properStateLocationSelected == 0) {
		$TheCLLocations[0] =~ s/'>/' selected>/gi;
		$location = $ShortCLlocations[0];
	}
	$craigsLocations = join "\n", @TheCLLocations;

	$craigsSort = '';
	foreach $clsort (@clSort) {
		$clsort =~ s/<\/option>//gi; $clsort =~ s/>//gi; $clsort =~ s/\r//gi;
		($clsort,$value,$name) = split(/"/,$clsort);
		$isSelected = '';
		if ($FORM{'sort'} eq $value) { $isSelected = 'selected'; }
		push(@TheCLSort,"<option value='$value' $isSelected>$name</option>");
	}
	$craigsSort = join "\n", @TheCLSort;

	#-$myloc = '&loc='.$FORM{'loc'}.'';
	$mypic = '&hasPic=0';
	$showt0 = '&showThumbs=0';
	$allc0 = '&multipleCities=0';
	$myQS = $ENV{'QUERY_STRING'};
	$myQS =~ s/$mypic//gi;
	$myQS =~ s/$showt0//gi;
	$myQS =~ s/$allc0//gi;
	#-$myQS =~ s/$myloc//gi;

	$elURL = 'http://www.craigslist.org/';

	$showImages = 'onload="javascript:CLoad();"';
	if ($shoth eq "checked") {
		$showImages = 'onload="javascript:ToggleCLimgs();CLoad();"';
	}

	##--/**v1**/
	##--$('span.ih').removeClass('ih').addClass('i').each(function(){if(\$(this).attr('id')){var iP=\$(this).attr('id').split(':');thumbURL='http://'+iP[0]+'.craigslist.org/thumb/'+iP[1];postURL=\$(this).siblings('a').attr('href');\$(this).html('<a target="Craigslist" href="'+postURL+'"><img alt="" src="'+thumbURL+'"></a>').mouseover(function(){var iP=\$(this).attr('id').split(':');fullURL='http://'+iP[0]+'.craigslist.org/'+iP[1];\$('#floater').html('<img src="'+fullURL+'">').show();}).mouseout(function(){\$('#floater').hide();}).mousemove(function(e){\$('#floater').css({'left':e.pageX+15+'px','top':e.pageY+15+'px'});})}})\$('#showImgs').hide();\$('#hideImgs').css('display','inline');var date=new Date();date.setTime(date.getTime()+(365*24*60*60*1000));document.cookie="cl_img=show; domain=craigslist.org; expires="+date.toGMTString()+"; path=/";

	print "Content-type: text/html\n\n";

	print qq~
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
	<!-- $myQS -->
	<head>
	<title>Craigslist SuperSearch (Beta) by MyVirtualPrivate (VPS-NET)</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	~; if ($myHead) { print $myHead; } print qq~
	<script src="../jquery-1.7.2.min.js"></script>
	<script type="text/javascript" language="JavaScript" src="../clss.js"></script>
	<link rel="stylesheet" type="text/css" href="../clss.css">
	<style style="text/css">
	/* INVALID CSS DECLARATION, MUST BE 'hidden' | 'block' not 0|1 */
	#showImgs { 
		display:$showThumbs;
	}
	.paginator {
		$paginator
	}
	.toc_legend {
		$toclegend
	}
	</style>
	</head>
	<body bgcolor="#E5E5E5" style="margin:0;padding:0px;" $showImages>

	<div>
	<div style="text-align:left;padding:1.6em;$noBotTopPad">
	<div id="content">
	<div id="datesearch"><fieldset style="margin:0 0 20px 0;"><legend style="font-weight:bold">NEW: In-Doc QuickSearch</legend><div style="margin:10px 10px 20px 10px;"><div style="margin:0 0 10px 0;">Just type and hit enter, if a listing matches your search, its shown, otherwise its hidden.</div><input type="text" value="" placeholder="Search, eg: Jan 21 OR 01-21"></div></fieldset></div>

	~;

	##-- SLS single or multiple [if multiple selected show multiple checkboxes]
	$allState = '0';
	$allChecks = '0';
	$foundRowDate = 0;
	$showHideStateLocationsList = '';
	if ($FORM{'multipleAreas'} eq "1") {
		$allState = 1;
		$allChecks = int(@TheCLLocationCheckboxes);
		$showHideStateLocationsList = 'display:none;';
		$myLocationCheckboxes = join '', @TheCLLocationCheckboxes;
	}

	require("../craigslistSearchForm.pl");

	#-- SINGLE SEARCH: ORIGINAL
	#-- print qq~ $myBody ~;

	###-- now search and print results
	#-- MULTI SEARCH
	##-- count how many times we've found span.date
	$cRowPad = 0;
	$allScripts = '';
	$cRuns = 0;
	if ($multiCities eq "1") {
		@myQS = split(/&/,$myQS);

		##-- statelocationselection single or multiple
		if ($FORM{'SLS'} ne "") {
			@ShortCLlocations = split(/, /,$FORM{'SLS'});
		}

		foreach $unLocale (@ShortCLlocations) {
			$thyBody = '';
			foreach $qspart (@myQS) {
				$mqs .= $myQS;
			}
			$thyBody = &runSearch($mqs, $unLocale, $cRuns);
			$cRuns++;

			##--pad left to overcome date placement [only need css once, not many times]
			$pRowPad = '';
			if ($thyBody =~ 'span class="date"' && $cRowPad == 0) {
				$cRowPad++;
				$pRowPad = 'padding-left:0;'; print "<style type=\"text/css\">span.pl, span.pl:hover { $pRowPad }</style>";
			}
			$mqs = "";
			print $thyBody;
		}
	}
	#-- SINGLE SEARCH: ORIGINAL
	else {
		$thyBody = &runSearch($myQS,$location, $cRuns);

		##--pad left to overcome date placement [only need css once, not many times]
		$pRowPad = '';
		if ($thyBody =~ 'span class="date"' && $cRowPad == 0) { 
			$cRowPad++;
			$pRowPad = 'padding-left:0;'; print "<style type=\"text/css\">span.pl, span.pl:hover { $pRowPad }</style>";
		}
		print $thyBody;
	}




	print qq~
			</div>
		</div>
	</div>
	</body>
	</html>
	~;





####---START runSearch
	sub runSearch {
		$runQS = $_[0];
		$myLocation = $_[1];
		$cRuns = $_[2];

		## SINGLE - orangecounty - query=&loc=orangecounty&catAbb=cpg&srchType=A&minAsk=&maxAsk=&sort=date
		## MULTIPLE - orangecounty - query=&loc=orangecounty&multipleAreas=1&catAbb=cpg&srchType=A&minAsk=&maxAsk=&sort=datequery=
		
		$myBodyStart = "<fieldset><legend><div style=\"font-weight:bold;\">$theLocationNames{$myLocation}, $cualstate</div></legend>";
		$searchURL = "http://$myLocation.craigslist.org/search/sss";
		$localURL = "http://$myLocation.craigslist.org/";
		$contentROOT = 'http://www.craigslist.org/search/';
		$reSearchURL = $searchURL.'?';

		$bp = $elURL; 
		## if base path doesn't have a trailing forward slash we need to add it
		if ((substr $bp, -1) ne $forsl) { $bp .= $forsl; }

		@myTruePath = split(/\//,$bp);
		pop(@myTruePath);
		$oneBack = join($forsl,@myTruePath);
		pop(@myTruePath);
		$twoBack = join($forsl,@myTruePath);

		$oneBackLoco = $oneBack;
		$oneBackLoco =~ s/$elURL//gi;
		$twoBackLoco = $twoBack;
		$twoBackLoco =~ s/$elURL//gi;

		$text = get("$searchURL?$runQS");
		$docloc = "$elURL".$ms;
		
		##-- setup the document for our parser
		##-- make sure HEAD BODY open & close ARE ON OWN LINE [splitting using newline]
		##-- do the same to P to cut off the logo from top
		$text =~ s/<head>/\n<head>\n/gi;
		$text =~ s/<\/head>/\n<\/head>\n/gi;
		$text =~ s/<body>/\n<body>\n/gi;
		$text =~ s/<\/body>/\n<\/body>\n/gi;
		$text =~ s/<p>/\n<\!--changed--><p>/gi;
		$text =~ s/<\/p>/<\/p><\!--changed-->\n/gi;

		$text =~ s/<div class=\"head\">/<div class=\"head\">\n/gi;

		#-- clean links [make them absolute based on remote path]
		my $count;
		my $resolver = HTML::ResolveLink->new(
			base => $bp,
			callback => sub {
				my($uri, $old) = @_;
				$count++;
			},
		);
		$text = $resolver->resolve($text);

		##-- split text into DocumentArray by newline
		my @elDocu = "";
		@elDocu = split(/\n/,$text);

		##-- get head contents
		my $myHead;
		foreach $_ (@elDocu){
			#-- some documents missing head closer [so cut it at body opener]
			if(/<HEAD>/i .. /<BODY/i ) {
				if ($_ ne '<head>' && $_ ne '</head>' && $_ !~ '<body') {
					$myHead .= $_ . "\n";
				}
			}
		}

		##-- get title [no longer needed but cool, so keep for later use] (now used to verify the existence of a title in the document, since some docs are missing head but have title, body and headContents)
		$p = HTML::TokeParser->new( \$text );
		if ($p->get_tag("title")) {
			$myTitle = $p->get_trimmed_text;
		}
		
		##-- get body contents
		my $myBody;
		foreach $_ (@elDocu){
			##- PRE-2017
			##-WAS:
			##- if(/<BODY/i .. /<\/BODY>/i ) {
			if(/<ul class="rows"/i .. /<\/ul>/i ) {
				##-WAS:
				##- if ($_ !~ '<BODY' && $_ ne '</BODY>' && $_ ne '</BODY>') {
				if ($_ !~ '<ul class="rows"' && $_ ne '</ul>' && $_ ne '</ul>') {
						##-- if inDocument ANCHOR :: these need to be escaped for a prematch \ . ^ $ * + ? { } [ ] ( ) |
						##-- EXAMPLES: <a name="anchorname" OR <a target="target" name="anchorname"
						# if ($_ =~ /(<a \b[^>]*>.*?<\/a>)/i && $_ =~ /( name=)/i) { $_ =~ s/(<a \b[^>]*>.*?<\/a>)/<span class="anchor-spacer">$1<\/span>/gi; }
						# if ($_ =~ /(<a \b[^>]*>.*?<\/a>)/i && $_ =~ 'class="i"' && $_ =~ 'data-id=' ) { $_ =~ s/(<a \b[^>]*>.*?<\/a>)/<span class="showImages">$1<\/span>/gi; }
						
						##-- considering we only need one set of scripts, load those at first run only, all subsequent runs don't parse scripts
						if ($_ =~ /(<script \b[^>]*>.*?<\/script>)/i && $_ =~ 'src' && $cRuns >= 1) { 
							$_ =~ s/(<script \b[^>]*>.*?<\/script>)//gi;
						}
						
						##-- query strings missing location and showThumbs, add em
						$myLoc = '?loc='.$myLocation.'&showThumbs='.$showThumbs.'&multipleCities='.$multiCities.'&catAbb';
						$_ =~ s/\?catAbb/$myLoc/g;

						##-- turn craigslist.org/index to craigslist.org/sss/index [for l18n]
						##$_ =~ s/org\/index/org\/sss\/index/g;
						
						##-- replace next 100[x] postings link with NOTHING
						if ($_ =~ '<a ' && $_ =~ 'next ' && $_ =~ ' postings') { $_ = ''; }
						elsif ($_ =~ '<a ' && $_ =~ ' name=') {
							##-- must assign an ID to anchors without, scrollTo
							@myLineAnch = split(/<a/,$_);
							foreach $MLA (@myLineAnch) {
								if ($MLA =~ 'name=' && $MLA !~ 'id=') {
									@myanch = split(/ /,$MLA);
									$newA = '';
									foreach $ma(@myanch) {
										if ($ma =~ 'name=') {
											$newA = 1;
											$elNom = $ma;
											my ($fi,$sec,$thir) = split(/"/,$elNom);
											$suNAME = 'name="'.$sec.'"';
											$newID = 'id="'.$sec.'"';
										}
									}
									if ($newA == 1) { $_ =~ s/$suNAME/$suNAME $newID/gi; }
								}
							}
						}

						$myBody .= "\n" . $_;
				}
			}
		}
		
		my $resultsList = $myBody;
		#-clear
		$myBody = "";
		
		#- added 2016, to remove document cross-contamination of inline scripting
		$resultsList =~ s/<script[^>]*>.*?<\/script>//igs;
		
		##-- didnt find head at first pass, head tag missing, but we found $resultsList [will test for title]
		if (!$myHead && $resultsList && (length($resultsList) > 0)) {

			##-- we found $myTitle 
			if (length($myTitle) > 0) {
				##-- only if we have a well formed title and existence of body open tag
				if ($text =~ '<title' && $text =~ '</title' && $text =~ '<body') {
					$text =~ s/<title>/\n<head>\n<title>/gi;
					$text =~ s/<body/\n<\/head>\n<body/gi;

					##-- try for head again
					@elDocu2 = split(/\n/,$text);
					foreach $_ (@elDocu2){
						if(/<HEAD>/i .. /<\/HEAD>/i ) {
							if ($_ ne '<head>' && $_ ne '</head>') {
								$myHead .= $_ . "\n";
							}
						}
					}
				}
			}
		}
		
		##-- didnt find head at 2nd pass and/or empty title and/or empty body
		if ($myHead && $resultsList && (length($myHead) <= 0 || length($resultsList) <= 0 || length($myTitle) <= 0)) {
			$myTitle = 'Redirecting to Craigslist: $docloc';
			$myHead = '<meta http-equiv="Refresh" content="URL=$docloc" \>';
			$resultsList = 'There was an error parsing this document, we are now forwarding you to its location at Craigslist.org';
			exit;
		}
		
		##-- clean up our changes to the original markup
		$resultsList =~ s/\n<\!--changed--><p>/<p>/gi;
		$resultsList =~ s/<\/p><\!--changed-->\n/<\/p>/gi;

		##--START: CLEANING DATA AND LINKS
			##-- clean the title remove unicode non-breaking space
			$myTitle =~ s/\xa0/ /gi;
			$myTitle =~ s/&nbsp;//gi;
			##-- just in case
			$myTitle =~ s/\n//gi;

			##- ONCE WE TAG it with our TARGET=, we've altered the link from its original format and will not alter it furthermore [finalized link]
			##-- inDocument ANCHORS will be resolving back to current URL/PAGE [won't request new doc from our server, simple jump down/up]
			##-- helps with MAP links and the like, makes them resolve...
			##-- but must remove _self at loadtime, switch to Craigslist as target
			$linkEXT1 = ' href="'.$bp.'#';
			$linkEXT1R = ' target="_self" href="#';
			$resultsList =~ s/$linkEXT1/$linkEXT1R/gi;

			##-- search results re-search using paging and other cl mechanisms
			$resultsList =~ s/$reSearchURL//gi;
			$resultsList =~ s/search\/sss?//gi;

			##-- sort by div customized for removal using css, not needed
			$resultsList =~ s/<div>sort by /<div id=sortByDiv>sort by /gi;
			
			##-- force new target on http://$myLocation.craigslist.org/ URIs
			$linkEXT2 = ' href="'.$localURL;
			$linkEXT2R = ' target="Craigslist" href="'.$localURL;
			$resultsList =~ s/$linkEXT2/$linkEXT2R/gi;

			##-- force new target on http://www.craigslist.org/ URIs
			##-- while flipping them to their proper locale at the same time [humbolt.craigslist.org]
			$linkEXT3 = ' href="'.$elURL;
			$linkEXT3R = ' target="Craigslist" href="'.$localURL;
			$resultsList =~ s/$linkEXT3/$linkEXT3R/gi;

			##-- all other /search/ urls
			$linkEXT3 = '<a href="'.$contentROOT;
			$linkEXT3R = '<a target="_self" href="?st=search/';
			$resultsList =~ s/$linkEXT3/$linkEXT3R/gi;
			
			##-- turn all non https to common route protocol
			$linkHTTP = 'http://';
			$linkHTTPR = '//';
			$resultsList =~ s/$linkHTTP/$linkHTTPR/gi;

			my $noBotTopPad = '';
			if ($resultsList=~"navbar") { $noBotTopPad = 'padding-top:0px;padding-bottom:0px;'; }

			$resultsList =~ s/[^[:ascii:]]+//g;
		##--END: CLEANING DATA AND LINKS
		
		return "$myBodyStart<div style=\"position:relative;top:0px;\"><ul class=\"rows\">$resultsList</ul></div> </fieldset>";
		
	}
###--END runSearch

exit;


