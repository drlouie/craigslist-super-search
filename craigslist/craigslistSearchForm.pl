print qq~
<form method="GET" id="CLFORM" name="CLFORM">
<span class="activeUserData"><span><nobr><input type="text" name="query" value="$FORM{'query'}">&nbsp;&nbsp;</nobr><nobr><input type="radio" name="srchType" id="srchTypeA" value="A" $stAsel><label for="srchTypeA">Entire Post</label>&nbsp;<input type="radio" name="srchType" id="srchTypeT" value="T" $stTsel><label for="srchTypeT">Title Only</label>&nbsp;</nobr></span></span>
<div style="clear:left;"></div>
<span class="activeUserData"><span><select name="catAbb" onChange="javascript:categoryChange(this);">$craigsList</select></span></span>
<div style="clear:left;"></div>
<div>
	<div style="float:left;"><span class="activeUserData"><span><select name="state" onChange="javascript:stateChange(this);">@clEstados</select></span></span></div>
	<div id="StateLocationList" style="float:left;width:auto;$showHideStateLocationsList"><span class="activeUserData"><span><select name="loc" id="StateLocations">$craigsLocations</select></span></span></div>
	<div style="clear:all;"><span class="activeUserData"><span><nobr><input type="checkbox" name="multipleAreas" id="multipleAreas" value="1" onChange="return clCheckboxes();" $multicit><label for="multipleAreas"><i id="AllMulti" style="font-style:normal;">$AllMulti</i> $cualstate <i id="Locations" style="font-style:normal;">$Locations</i></nobr></label></span></span></div>
</div>
<div id="clChecks" style="width:100%;">$myLocationCheckboxes</div>
<div style="clear:left;"></div>
<span class="activeUserData"><span><nobr><label for="minAsk">Min Price </label><input type="text" name="minAsk" id="minAsk" value="$FORM{'minAsk'}">&nbsp;</nobr><nobr><label for="maxAsk">Max Price </label><input type="text" name="maxAsk" id="maxAsk" value="$FORM{'maxAsk'}">&nbsp;</nobr></span></span>
<div style="clear:left;"></div>
<div id="dateRange" style="width:100%;">$myDatesInResults</div>
<div style="clear:left;"></div>
<!--<nobr><label for="sort">Sort By</label> <select name="sort" id="sort">$craigsSort</select>&nbsp;</nobr>-->
<span class="activeUserData">Duplicates:
<nobr><input type="radio" name="duplicateAction" id="showDupes" value="show" onChange="ToggleDuplicates('show');"><label for="showDupes">Show</label>&nbsp;</nobr>
<nobr><input type="radio" name="duplicateAction" id="hideDupes" value="hide" onChange="ToggleDuplicates('hide');"><label for="hideDupes">Hide</label>&nbsp;</nobr>
<nobr><input type="radio" name="duplicateAction" id="flagDupes" value="flag" onChange="ToggleDuplicates('flag');"><label for="flagDupes">Flag</label>&nbsp;</nobr>
</span>
<div style="clear:left;"></div>
<span class="activeUserData"><span><nobr><input type="checkbox" name="hasPic" id="hasPic" value="1" $hssel><label for="hasPic">Has Photo</label>&nbsp;</nobr><nobr><input type="checkbox" name="showThumbs" id="showThumbs" value="1" onChange="ToggleCLimgs();" $shoth><label for="showThumbs">Show Thumbnails</label>&nbsp;</nobr><br></span></span>
<div style="clear:left;"></div>
<input type="submit" value="Search Craigslist">

</form>
<script language="Javascript" type="text/javascript">
var stateChange = function(who) {
	\$("select#StateLocations").val(''); 
	\$("#multipleAreas").removeAttr('checked');
	\$("#CLFORM").submit();
};
var allChecks = $allChecks;
var allChecked = $allChecked;
var locChange = function(who) {
	if (who.checked == 1) { allChecked++; }
	else { allChecked--; }
	if (allChecked == 0) {
		\$("#AllMulti").html('All');
		\$("#Locations").html('Locations');
	}
	else {
		\$("#AllMulti").html('Selected');
		if (allChecked == 1) { \$("#Locations").html('Location'); }
		else { \$("#Locations").html('Locations'); }
	}
};

var categoryChange = function(craigslist_category) {var craigslist_super_search_category='';var craigslist_super_search_directory='craigslist';var craigslist_super_search_category_selected = craigslist_category.options[craigslist_category.selectedIndex].value;var vps_net_directory = ''+document.location+'';if (craigslist_category.selectedIndex <= 8) {if (craigslist_super_search_category_selected == 'bbb' && !(vps_net_directory.indexOf('services') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/services/'; }else if (craigslist_super_search_category_selected == 'ccc' && !(vps_net_directory.indexOf('community') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/community/'; }else if (craigslist_super_search_category_selected == 'eee' && !(vps_net_directory.indexOf('events') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/events/'; }else if (craigslist_super_search_category_selected == 'ggg' && !(vps_net_directory.indexOf('find-work') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/find-work/'; }else if (craigslist_super_search_category_selected == 'jjj' && !(vps_net_directory.indexOf('find-work') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/find-work/'; }else if (craigslist_super_search_category_selected == 'hhh' && !(vps_net_directory.indexOf('find-a-home') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/find-a-home/'; }else if (craigslist_super_search_category_selected == 'ppp' && !(vps_net_directory.indexOf('find-a-mate') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/find-a-mate/'; }else if (craigslist_super_search_category_selected == 'sss' && !(vps_net_directory.indexOf('want-to-find') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/want-to-find/'; }else if (craigslist_super_search_category_selected == 'res' && !(vps_net_directory.indexOf('want-to-find') != -1)) { craigslist_super_search_category = '/'+craigslist_super_search_directory+'/want-to-find/'; }if (craigslist_super_search_category != '') { \$("#CLFORM").attr('action',craigslist_super_search_category).submit(); craigslist_super_search_category = ''; }}};
var allState = $allState;
var clCheckboxes = function() {
	var estado=document.CLFORM["loc"];
	for (var i=0; i<estado.options.length; i++) {
		allChecks++;
		if (estado.options[i].value != '' && allChecks < estado.options.length+1) {
			\$("#clChecks").append("<span class='activeLocationData'><span><input type='checkbox' name='SLS' value='"+estado.options[i].value+"' id='"+estado.options[i].value+"' onChange='javascript:locChange(this);'><label for='"+estado.options[i].value+"'> "+estado.options[i].text+"</label></span></span>");
		}
	}

	if (allState == 0) {
		\$("#StateLocationList").hide();
		\$("#clChecks").show();
		\$("#multipleAreas").attr('checked','checked');
		allState = 1;
	}
	else {
		\$("#StateLocationList").show();
		\$("#clChecks").hide();
		\$("#multipleAreas").removeAttr('checked');
		allState = 0;
	}

};
//- overcome CL JS errors
var areaID = '';
var pID = '';
var showMapTabs = function() {};
</script>
~;

1;