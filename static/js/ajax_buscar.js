$(function(){
function equalHeight(group) {
  var tallest = 0;
  group.each(function() {
    var thisHeight = $(this).height();
    if(thisHeight > tallest) {
      tallest = thisHeight;
    }
  });
  group.height(tallest);
}
equalHeight($(".box-1 .inner"));


$("#tags1").autocomplete({
  minLength:3,
  source: function(req, add){
    var search=$("#tags1").val();
    $.ajax({
      url:'{% url 'biblioteca:algobuscar' %}',
      async:false,
      dataType:'json',
      type:'GET',
      data:{ 'start': search,},
      success: function(data){
        var suggestions=[];

        $.each(data, function(index, objeto){
          suggestions.push(objeto.nombre);
        });

        add(suggestions);
      },
      error:function(err){
        alert("error");
      }
    });
  }
});

});
