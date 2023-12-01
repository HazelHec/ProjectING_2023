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

  /**
   * Metodo para graficas backpressure
   */
  const chartContext1 = document.getElementById("myChart").getContext("2d");
  const chartContextModal1 = document
    .getElementById("modalChart1")
    .getContext("2d");
  // Valores iniciales
  const initialData = {
    labels: [10, 20, 30, 20, 10],
    datasets: [
      {
        label: "Vogel",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
        data: [10, 20, 30, 20, 10],
        fill: false,
        tension: 0.4,
      },
    ],
  };
  const chartOptions = {
    scales: {
      x: {
        type: "logarithmic",
        title: {
          display: true,
          text: "Qo (Logarítmico)",
        },
      },
      y: {
        type: "logarithmic",
        title: {
          display: true,
          text: "Pwf (Logarítmico)",
        },
        beginAtZero: true,
      },
    },
  };
  var myChart = new Chart(chartContext1, {
    type: "line", // Cambiado a tipo de gráfico de línea para mejorar la visualización logarítmica
    data: initialData,
    options: chartOptions,
  });
  var myChartModal = new Chart(chartContextModal1, {
    type: "line", // Cambiado a tipo de gráfico de línea para mejorar la visualización logarítmica
    data: initialData,
    options: chartOptions,
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

    $.ajax({
      type: "POST",
      url: "/productividad/back-pressure",
      data: JSON.stringify(dataEnv),
      contentType: "application/json",
      dataType: "JSON",
      success: done,
      error: errorGraphic,
    });

    function done(result) {
      console.log(result);
      imprimirResultados(result);

      const newData = {
        labels: result.lqg,
        datasets: [
          {
            label: "BackPressure",
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1,
            data: result.lpwf,
            tension: 1,
          },
        ],
      };
      myChart.data = newData;
      myChart.update();
      myChartModal.data = newData;
      myChartModal.update();
    }
    function errorGraphic(error) {
      alert(error.message);
    }

    function imprimirResultados(data) {
      const contenedor = document.getElementById("results");
      contenedor.innerHTML = ""; // Limpiar contenido anterior
      const divResultado = document.createElement("div");

      $.each(data, function (key, value) {
        const pElement = document.createElement("p");
        pElement.textContent = `${key}: ${JSON.stringify(value)}`;
        divResultado.appendChild(pElement);
      });

      contenedor.appendChild(divResultado);
    }
  });
});
