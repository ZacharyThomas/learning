var express = require("express");

var app = express()

app.set('views',__dirname + '/views')
app.use(express.static(__dirname + '/public'))

app.get('/',function(req,res){
	res.render('index')
})

console.log("listening on port 3000...")
app.listen(3000)
