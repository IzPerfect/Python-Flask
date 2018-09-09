var Body = {
  setColor:function(color){
    document.querySelector('#change').style.color = color;
  },
  setBackgroundColor:function(color){
    document.querySelector('#change').style.backgroundColor = color;
  }
}


function styleChanger(self){
  var target = document.querySelector('body');
  if(self.value == 'black'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    self.value = 'white'
  } else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    self.value = 'black'
  }
}
