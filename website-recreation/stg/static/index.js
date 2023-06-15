

window.onscroll = function() {
    var div = document.getElementById("nav");
    if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
        div.style.backgroundColor = "rgb(255, 255, 255,1)";    } else {
      div.style.backgroundColor = "rgb(255, 255, 255,0.8)";
    }
  }
   function val(){

      var mobile = document.getElementById("mob").value;
      var mail = document.getElementById("mail").value;
			
			var mobileRegex = /^[0-9]{10}$/;
      var emailRegex = /^[^\s]+@[^\s]+\.[^\s]+$/;
			if (!mobile.match(mobileRegex)) {
				alert("Please Enter only Indian mobile number without the country code");
				return false;
			}
      if (!mail.match(emailRegex)) {
				alert("Please Enter Valid Email ID");
				return false;
			}


			return alert("Thanks for the feedback"); // Form is valid
   }

   

//   var data=[10,20,30,40];
// console.log(data);
// var barh=100;
// var incw=60;
// var barx=10;
// var baryc=10;
// var graph=d3.select('svg')
// 	.attr("width",1500)
// 	.attr("height",barh*(data.length+1))
// for(var i=0;i<data.length;i++){
// graph.select('g')
// 	.append('rect')
// 	.attr("x",barx)
// 	.attr("y",baryc)
// 	.attr("width",(data[i]+1)*incw)
// 	.attr("height",barh)
// graph.select('g')
// 	.append('text')
// 	.attr("x",barx+10)
// 	.attr("y",baryc+(barh/2))
// 	.text("Party "+(i+1)+" : "+data[i])
// baryc+=barh;
// }