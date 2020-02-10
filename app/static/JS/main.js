//Faz a alternância de navegação funcionar em telas menores.
$(document).ready(function(){
	$('#nav-menu').click(function(){
		$('ul.nav-list').addClass('open').slideToggle('200');
	});
});