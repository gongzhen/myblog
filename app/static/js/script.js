/*

My Custom JS
============

Author:  Brad Hussey
Updated: August 2013
Notes:	 Hand coded for Udemy.com
http://stackoverflow.com/questions/11533542/twitter-bootstrap-add-active-class-to-li
http://stackoverflow.com/questions/16856287/set-link-of-my-navbar-active-with-bootstap
http://stackoverflow.com/questions/9301507/bootstrap-css-active-navigation

*/

$(document).ready(function () {
    var url = window.location;
	// Will only work if string in href matches with location
    $('ul.nav a[href="' + url + '"]').parent().addClass('active');
    $('.nav li').removeClass('active');
    // Will also work for relative and absolute hrefs
    $('ul.nav a').filter(function () {
        return this.href == url;
    }).parent().addClass('active');
});