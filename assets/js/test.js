console.log("hola mundo");
dataEnv = {
  qo: 200,
  pr: 4000,
  pwf: 3000,
  pb: 2000,
  r: 30
};
let response = $.ajax({
  type: "POST",
  url: "/productividad/vogel",
  data: JSON.stringify(dataEnv),
  contentType: "application/json",
  dataType: "JSON",
});
response.done(function(result) {
  console.log(result);
});
response.fail(function(error){
  console.log(error);
});





// const btn = document.getElementById("enviar");
// btn.addEventListener("click", function () {
//   let dataEnv = {
//     qo: parseFloat(document.getElementById("qo").value),
//     pr: parseFloat(document.getElementById("pr").value),
//     pwf: parseFloat(document.getElementById("pwf").value),
//     pb: parseFloat(document.getElementById("pb").value),
//     r: parseInt(document.getElementById("r").value),
//   };
//   console.log(typeof dataEnv);
//   console.log(typeof dataEnv["qo"]);
//   for (let key in dataEnv) {
//     console.log(typeof dataEnv[key]);
//   }

//   let request = $.ajax({
//     type: "POST",
//     url: "/productividad/vogel",
//     data: JSON.stringify(dataEnv),
//     dataType: "JSON",
//   });

//   request.done(function (response) {
//     console.log(response);
//   });
// });
// let request = $.ajax({
//     type: "post",
//     url: "/productividad/vogel",
//     data: "data",
//     dataType: "JSON",
// });
// request.done(function(response){

// });
