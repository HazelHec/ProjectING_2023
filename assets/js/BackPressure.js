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
    pr: document.getElementById("pws").value,
    pwf1: document.getElementById("pwf1").value,
    pwf2: document.getElementById("pwf2").value,
    qg1: document.getElementById("qg1").value,
    qg2: document.getElementById("qg2").value,
    r: document.getElementById("r").value,
  };

  let request = $.ajax({
    type: "POST",
    url: "/productividad/back-pressure",
    data: JSON.stringify(dataEnv),
    contentType: "application/json",
    dataType: "JSON",
  });

  request.done(function (result) {
    console.log(result);
    graficar(result.lqg, result.lpwf);
  });

  request.fail(function (error) {
    alert(error.message);
  });
});

function graficar(x,y) {
  try {
    myChart.destroy();
  } catch (e) {
    console.error(e);
  }
  pwf = y;
  qo = x;
  // Datos del gráfico
  var chartData = {
    labels: qo,
    datasets: [
      {
        label: "IPR",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
        data: pwf,
        fill: false,
      },
    ],
  };

  // Configuración del gráfico
  var chartOptions = {
    responsive: true,
    scales: {
      x: {
        title: {
          display: true,
          text: "Qo",
        },
      },
      y: {
        title: {
          display: true,
          text: "Pwf",
        },
      },
    },
  };

  // Crear el gráfico
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "line",
    data: chartData,
    options: chartOptions,
    legend: {
      display: true,
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
  });
}
