document.addEventListener("DOMContentLoaded", function () {
  const nav = document.querySelector("#nav");
  const abrir = document.querySelector("#abrir");
  const cerrar = document.querySelector("#cerrar");

  abrir.addEventListener("click", () => {
    nav.classList.add("visible");
  });

  cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
  });
});

//Instanciar boton
const enviar = document.getElementById("calcular");
enviar.addEventListener("click", function () {
  dataEnv = {
    qo: document.getElementById("qo").value,
    prP: document.getElementById("prP").value,
    pwf: document.getElementById("pwf").value,
    prF: document.getElementById("prF").value,
  };

  let request = $.ajax({
    type: "POST",
    url: "/productividad/eickmeier",
    data: JSON.stringify(dataEnv),
    contentType: "application/json",
    dataType: "JSON",
  });

  request.done(function (result) {
    console.log(result);
    // dataGraphics = Object.assign({}, result.lqob, result.lqos);
    // graficar(dataGraphics);
  });

  request.fail(function (error) {
    alert(error.message);
  });
});

// function graficar(data) {
//   try {
//     myChart.destroy();
//   } catch (e) {
//     console.error(e);
//   }
//   pwf = Object.keys(data);
//   qo = Object.values(data);
//   // Datos del gráfico
//   var chartData = {
//     labels: qo,
//     datasets: [
//       {
//         label: "IPR",
//         backgroundColor: "rgba(75, 192, 192, 0.2)",
//         borderColor: "rgba(75, 192, 192, 1)",
//         borderWidth: 1,
//         data: pwf,
//         fill: false,
//       },
//     ],
//   };

//   // Configuración del gráfico
//   var chartOptions = {
//     responsive: true,
//     scales: {
//       x: {
//         title: {
//           display: true,
//           text: "Qo",
//         },
//       },
//       y: {
//         title: {
//           display: true,
//           text: "Pwf",
//         },
//       },
//     },
//   };

//   // Crear el gráfico
//   var ctx = document.getElementById("myChart").getContext("2d");
//   var myChart = new Chart(ctx, {
//     type: "line",
//     data: chartData,
//     options: chartOptions,
//     legend: {
//       display: true,
//     },
//     tooltips: {
//       mode: "index",
//       intersect: false,
//     },
//   });
// }
