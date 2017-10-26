	var IveSeenPID = '';
	var hDs = 0;
	var ToggleDuplicates = function(state) {
		if (state == 'hide'){hDs=1;}
		else if (state == 'flag'){hDs = 2;}
		else{hDs = 0;}
		IveSeenPID='';
		$('li.result-row').each(function(){
			var cA=$(this);var MyPID=''+cA.attr('data-pid')+'';
			if(MyPID!=''&&IveSeenPID.indexOf(':'+cA.attr('data-pid')+':')==-1){IveSeenPID+=':'+cA.attr('data-pid')+':';}
			else{
				if(hDs == 2){cA.show();cA.fadeTo('slow','.4');$("#flagDupes").prop('checked','checked');}
				else if(hDs == 1){cA.fadeTo('fast','0.0');cA.hide();$("#hideDupes").prop('checked','checked');}
				else{cA.show();cA.fadeTo('fast','1.0');$("#showDupes").prop('checked','checked');}
			}
		});
	};
	var IveSeenDate = '';
	var AllMyDates = new Array();
	var DefineDateRange = function() {
		var TheMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
		var Today = new Date();
		var TodayD = Today.getDate();
		var TodayM = Today.getMonth()+1;
		var TodayY = Today.getFullYear();
		var CurrentMonthDates = new Array();
		var AllOtherMonthsDates = new Array();
		var SeenMonth = '';
		var DefineMonths = new Array();
		var DateCheckbox = "<span class='activeDateData'><span><input type='checkbox' name='ActiveDateRange' value='%%VALUE%%' id='%%VALUE%%' %%DATESELECTED%%><label for='%%VALUE%%'>%%VALUE%%</label></span></span>";
		$('p.row span.date').each(function(){
			var MyDate = ''+$(this).html()+'';
			MyMonth = MyDate.substring(0,3);
			if (!isNaN(MyDate.substring(MyDate.length - 2))) {
				MyDay = MyDate.substring(MyDate.length - 2);
			}
			else {
				MyDay = MyDate.substring(MyDate.length - 1);
			}

			MyDate = ''+MyMonth+' '+Number(MyDay)+'';

			if (MyDate != '' && IveSeenDate.indexOf(':'+MyDate+':') == -1) {
				/* current months' dates seen */
				var TheAdDate = new Date(''+TheMonths[Today.getMonth()]+' '+MyDay+', '+TodayY+' 00:00:01');
				if (MyMonth == TheMonths[Today.getMonth()].substring(0,3)) {
					CurrentMonthDates.push(TheAdDate);
				}

				/* if computed date is later than today, must be previous year, for instance december, november of previous year */
				TryDate = new Date(''+MyMonth+' '+MyDay+', '+TodayY+' 00:00:01');
				/* only if not a current month date */
				if (MyMonth != TheMonths[Today.getMonth()].substring(0,3)) {
					/* date is after 'current date', make it right*/
					if (TryDate > TheAdDate) { RightDate = new Date(''+MyMonth+' '+MyDay+', '+(TodayY-1)+' 00:00:01'); }
					/* date is good to go as is */
					else { RightDate = new Date(''+MyMonth+' '+MyDay+', '+TodayY+' 00:00:01'); }
					AllOtherMonthsDates.push(RightDate);
				}
				/* tracking */
				IveSeenDate += ':'+MyDate+':';
				AllMyDates.push(MyDate);
				
			}
			/* set rel for later use, hence showing/hiding based on processed data */
			$(this).parent().parent().attr('rel',MyDate);
		});

		if (CurrentMonthDates.length >= 1) {
			CurrentMonthDates.sort(SortDatesDescending);
			for (var i=0; i<CurrentMonthDates.length; i++) {
				//"<span class='activeDateData'><span><input type='checkbox' name='ActiveDateRange' value='%%VALUE%%' id='%%VALUE%%' onChange='javascript:dateRangeChange(this);' %%DATESELECTED%%><label for='%%VALUE%%'>%%VALUE%%</label></span></span>";
				MyDateCheckbox = DateCheckbox.replace('%%DATESELECTED%%','').replace(/%%VALUE%%/g,TheMonths[CurrentMonthDates[i].getMonth()].substring(0,3)+' '+CurrentMonthDates[i].getDate());
				$("#dateRange").html(''+$("#dateRange").html()+''+MyDateCheckbox+'');
			}
		}
		if (AllOtherMonthsDates.length >= 1) {
			AllOtherMonthsDates.sort(SortDatesDescending);
			for (var i=0; i<AllOtherMonthsDates.length; i++) {
				var ProcessingMonth = TheMonths[AllOtherMonthsDates[i].getMonth()].substring(0,3);
				if (SeenMonth.indexOf(':' + ProcessingMonth + ':') == -1) {
					SeenMonth += ':'+ProcessingMonth+':';
					DefineMonths.push(ProcessingMonth);
				}
			}
			if (DefineMonths.length > 1) {
				for (var i=0; i<DefineMonths.length; i++) {
					for (var i2=0; i2<AllOtherMonthsDates.length; i2++) {
						if (DefineMonths[i] == TheMonths[AllOtherMonthsDates[i2].getMonth()].substring(0,3)) {
							MyDateCheckbox = DateCheckbox.replace('%%DATESELECTED%%','').replace(/%%VALUE%%/g,TheMonths[AllOtherMonthsDates[i2].getMonth()].substring(0,3)+' '+AllOtherMonthsDates[i2].getDate());
							$("#dateRange").html(''+$("#dateRange").html()+''+MyDateCheckbox+'');
						}
					}
				}
			}
			/* if not more than a single month (past), parse it as is */
			else if (DefineMonths.length == 1) {
				for (var i=0; i<AllOtherMonthsDates.length; i++) {
					MyDateCheckbox = DateCheckbox.replace('%%DATESELECTED%%','').replace(/%%VALUE%%/g,TheMonths[AllOtherMonthsDates[i].getMonth()].substring(0,3)+' '+AllOtherMonthsDates[i].getDate());
					$("#dateRange").html(''+$("#dateRange").html()+''+MyDateCheckbox+'');
				}
			}
		}

		var AllDatesCombined = new Array();
		$(".activeDateData input").change(function(){
			AllDatesCombined = [];
			for (var i=0; i<CurrentMonthDates.length; i++) { AllDatesCombined.push(CurrentMonthDates[i]); }
			for (var i=0; i<AllOtherMonthsDates.length; i++) { AllDatesCombined.push(AllOtherMonthsDates[i]); }
			
			/*reset the stage*/
			var findPivot = -1;
			$('p[rel]').each(function(){ $(this).show(); });
			$('span.activeDateData').each(function(){ $(this).fadeTo('fast','1.00'); });

			/* mark the stage*/
			for (var i=0; i<AllDatesCombined.length; i++) { 
				if (findPivot == -1 && TheMonths[AllDatesCombined[i].getMonth()].substring(0,3) + ' ' + AllDatesCombined[i].getDate() == $(this).attr('id')) {
					findPivot = i;
				}
				if (findPivot >= 0 && i > findPivot) {
					$("input#"+TheMonths[AllDatesCombined[i].getMonth()].substring(0,3) + ' ' + AllDatesCombined[i].getDate()+"").parent().parent().fadeTo('slow','0.30');

					$('span.activeDateData').each(function(){ 
						if ($(this).find('input').attr('id') == TheMonths[AllDatesCombined[i].getMonth()].substring(0,3) + ' ' + AllDatesCombined[i].getDate()) {
							$(this).fadeTo('fast','0.30'); 
						}
					});

					$('p[rel]').each(function(){
						if ($(this).attr('rel') == TheMonths[AllDatesCombined[i].getMonth()].substring(0,3) + ' ' + AllDatesCombined[i].getDate()) {
							//alert(TheMonths[AllDatesCombined[i].getMonth()].substring(0,3) + ' ' + AllDatesCombined[i].getDate());
							//alert($(this).attr('rel'));
							$(this).hide();
						}
					});
				}
			}
		});
	};
	var SortDatesAscending = function (d1, d2) {
	  if (d1 > d2) return 1;
	  if (d1 < d2) return -1;
	  return 0;
	};
	var SortDatesDescending = function (d1, d2) {
	  if (d1 > d2) return -1;
	  if (d1 < d2) return 1;
	  return 0;
	};
	var CLoad=function(){
		DefineDateRange();
		jQuery('.result-row a').each(function(){
			if(jQuery(this).attr('target') || !jQuery(this).attr('target')){
				jQuery(this).attr('target','Craigslist');
			}
		});
		$('h4.ban').each(function(){
			if($(this).attr('class')!='ban'){
				$(this).html('');
			}
			$(this).css('position','inline').css('left','-10px').css('display','block');
		});
		$('.button.next').each(function(){
			CreatePaginationLink($(this));
		});
		$('.button.prev').each(function(){
			CreatePaginationLink($(this));
		});
		$('.button.first').each(function(){
			$(this).removeAttr('href').removeAttr('target').css('text-decoration','underline').css('cursor','pointer').click(function(){
				$("#CLFORM").submit();
			});
		});
		
		/* date search, aka in-document list search, can search by dates, keywords or phrases, hiding all non-matching and only showing matching */
		jQuery("#datesearch").show();
		jQuery("#datesearch input").keyup(function(e){
			if (e.keyCode == 13) {
				jQuery('li[class="result-row"]').each(function(){
					var SearchContents = jQuery(this).html().toString();
					var SearchString = jQuery("#datesearch input").val();
					if (SearchContents.toLowerCase().indexOf(SearchString.toLowerCase()) != -1) {
						jQuery(this).show();
					}
					else {
						jQuery(this).hide();
					}
				});
			}
		});	
		
	};

	var CreatePaginationLink = function(that){
		var PaginationHref = ''+$(that).attr('href')+'';
		var DocHref = document.location.href;
		var UniquePagination=PaginationHref.split('&').filter(function(item,i,allItems){ return i==allItems.indexOf(item); }).join('&');
		var DefinePagination = UniquePagination.split('?');
		var DefineHREF = DocHref.split('?');
		var MergeUnique = DefinePagination[1] + '&' + DefineHREF[1];
		var MakeUniquePagination=MergeUnique.split('&').filter(function(item,i,allItems){ return i==allItems.indexOf(item); }).join('&');
		$(that).attr('href',''+ DefineHREF[0] +'?'+ MakeUniquePagination + '').removeAttr('target');
	};

	var showingImages=0;
	var mystyle='width:100%;margin:0;float:left;padding:0 0 0.62em 0;';
	var noImage='<div style="float:left;width:50px;height:50px;overflow:hidden;clip:rect(0px,50px,50px,0px,);" class="CLimage" title="This Craigslist ad has no thumbnail, but may still have a photo."><center>-</center></span>';
	var ToggleCLimgs=function(){
		var myImage=noImage;
		if(showingImages==0){
			$('a.result-image').each(function(){
				myImage=noImage;
				if($(this).attr('data-ids')){
					if(!($(this).attr('data-ids').indexOf('1:')!=-1)){myImage=noImage;}
					else{
						trueImage = $(this).attr('data-ids').split('1:');
						myImage='<img align="left" src="//images.craigslist.org/'+trueImage[1].replace(',','')+'_50x50c.jpg" class="CLimage">';
					}
				}
				$(this).html(myImage);
				if($(this).parent().attr('class')!='dynimage'){
					$(this).parent().html('<div class="dynimage" style="'+mystyle+'">'+$(this).parent().html()+'</div>');
				}
				else{	
					$(".dynimage").attr('style',mystyle);
					$(this).show();
				}
			});
			showingImages=1;
		}
		else{
			$('.CLimage').each(function(){
				$(".dynimage").attr('style','');
				$(this).hide();
			});
			showingImages=0;
		}
	};
