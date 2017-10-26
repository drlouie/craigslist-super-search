#!/usr/bin/perl5 -s

print "Content-type: text/html\n\n";

require("q.pl");

$WhichMessageTitle1 = 'Super';
$WhichMessageTitle2 = 'Search';
$WhichMessage = 'craigslist';
$WhichAltMessage = 'Craigslist SuperSearch (Beta) by Virtual Private Servers and Networks [VPS-NET]';
print qq~
<!-- $WhichAltMessage -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<head>
<title>$WhichAltMessage</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Refresh" content="5;url=/craigslist/want-to-find/">
<meta name="keywords" content="craigslist supersearch, craigslist super search, craigslist search by state, craigslist multiple city search, craigslist quick search, craigslist advanced search">
<meta name="description" content="Craigslist SuperSearch allows you to quickly search one or more locations in a state by allowing the selection of multiple cities and locations seamlessly.">
<style type="text/css">
body { background:#F7F7F7 url(./electrostatic.png) 0 0 repeat; margin:0; padding:0px; overflow-y:hidden; overflow-x:hidden; border:0; }
#vps { margin:0; padding:0px; overflow-y:hidden; overflow-x:hidden; border:0; position:absolute;left:0px;top:0px;visibility:visible;z-index:1;width:100%;height:100%; }
#net { background:url(/web_design_imagery/preloadBacker.gif) repeat-x 0 0; }
#virtual-private-servers-and-networks { width:48px;height:54px; overflow:hidden; background:url(/web_design_imagery/anilogo.gif) no-repeat; }
font{color:#000000;}
a:hover{color:#CC0000}
$cs1
$cs2
$cs3
</style>
</head>
<body bgcolor="#FFFFFF" text="#000000" link="#414477" alink="#414477" vlink="#666666">
<div style="width:1px;height:1px;visibility:hidden;overflow:hidden;clip:rect(1px,1px,1px,1px);color:#FFFFFF;font-size:1px;" title="Virtual Private Servers - Virtual Private Networks - Cloud Applications - Cloud Servers - Website Design - Web Development - Internet Design - Internet Applications - Information Technology - IT Development - Social Networks - Systems Engineering - Search Engine Optimization">Virtual Private Servers - Virtual Private Networks - Cloud Applications - Cloud Servers - Website Design - Web Development - Internet Design - Internet Applications - Information Technology - IT Development - Social Networks - Systems Engineering - Search Engine Optimization</div>
<div id="vps">
	<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0">
		<tr valign="middle"><td width="100%">
			<table width="100%" border="0" cellpadding="0" cellspacing="0">
				<tr><td width="100%" align="center" style="height:64px;padding: 1px 1px 0px 0px;"><div id="virtual-private-servers-and-networks" title="VPS-NET: Virtual Private Servers and Networks" style="cursor:help;"><img src="/web_design_imagery/spacer.gif" width="48" height="54" alt="VPS-NET: Virtual Private Servers and Networks" border="0"></div></td></tr>
				<tr style="cursor:wait;"><td width="100%" bgcolor="#C9CDDF"><img src="/web_design_imagery/spacie.gif" height="1" width="1" border="0" alt="Virtual Private Servers - VPS"></td></tr>
				<tr style="cursor:wait;"><td width="100%" bgcolor="#FFFFFF"><img src="/web_design_imagery/spacie.gif" height="1" width="1" border="0" alt="Virtual Private Networks - VPN"></td></tr>
				<tr style="cursor:wait;"><td width="100%" align="center" id="net" style="height:100px;color:#333333;letter-spacing:2px;font-family:verdana,arial;font-size:9px;" title="$WhichAltMessage" valign="middle"><div style="font-size:10px;"><div style="font-size:28px;letter-spacing:1px;padding-bottom:8px;font-family:times,tahoma;">$WhichMessage</div><b>$WhichMessageTitle1<font style="color:#266899">$WhichMessageTitle2</font></b></div></td></tr>
				<tr style="cursor:wait;"><td width="100%" bgcolor="#FFFFFF"><img src="/web_design_imagery/spacie.gif" height="1" width="1" border="0" alt="Application Programming Interface - API"></td></tr>
				<tr style="cursor:wait;"><td width="100%" bgcolor="#C9CDDF"><img src="/web_design_imagery/spacie.gif" height="1" width="1" border="0" alt="Search Engine Optimization - SEO"></td></tr>
			</table>
		</td></tr>
	</table>
</div>
<div style="width:1px;height:1px;visibility:hidden;overflow:hidden;clip:rect(1px,1px,1px,1px);color:#FFFFFF;font-size:1px;" title="Search Engine Optimization - Systems Engineering - Social Networks - IT Development - Information Technology - Internet Applications - Internet Design - Web Development - Website Design - Cloud Servers - Cloud Applications - Virtual Private Networks - Virtual Private Servers">Search Engine Optimization - Systems Engineering - Social Networks - IT Development - Information Technology - Internet Applications - Internet Design - Web Development - Website Design - Cloud Servers - Cloud Applications - Virtual Private Networks - Virtual Private Servers</div>
</body>
</html>
<!-- design, websites, hosting, applications, cloud, vpn, vps, virtual private, networks, servers, -->
~;

exit;
