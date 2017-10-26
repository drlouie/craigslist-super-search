if ($ENV{'REQUEST_METHOD'} eq 'GET'){@pairs=split(/&/, $ENV{'QUERY_STRING'});}elsif($ENV{'REQUEST_METHOD'} eq 'POST'){read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});@pairs=split(/&/, $buffer);}else{0;}foreach $pair (@pairs){local($name, $value) = split(/=/, $pair);$name =~ tr/+/ /;$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;if($value){$value =~ tr/+/ /;$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;$value =~ s/<!--(.|\n)*-->//g;}if ($FORM{$name} && $value){push(@Todo_Form,"$name-----$value");$FORM{$name}="$FORM{$name}, $value";}elsif($value){push(@Todo_Form,"$name-----$value");push(@Field_Order,$name);$FORM{$name}=$value;}}
##-->> sanitize
foreach $afi (@FORM) {$afi =~ s/'//gi;$afi =~ s/"//gi;$afi =~ s/%//gi;}

1;