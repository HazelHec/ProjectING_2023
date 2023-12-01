document.addEventListener("DOMContentLoaded", function () {
  const abrir = document.querySelector("#abrir");
  const cerrar = document.querySelector("#cerrar");
  abrir.addEventListener("click", () => {
    nav.classList.add("visible");
  });
  cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
  });
  /**
   *
   *
   */
  const chartContext1 = document.getElementById("myChart").getContext("2d");
  const chartContext2 = document.getElementById("myChart2").getContext("2d");
  const chartContextModal1 = document
    .getElementById("modalChart1")
    .getContext("2d");
  const chartContextModal2 = document
    .getElementById("modalChart2")
    .getContext("2d");
  // Crear gráfico inicial
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
    responsive: true,
    scales: {
      x: {
        title: {
          display: true,
          text: "Qo (Gasto)",
        },
      },
      y: {
        title: {
          display: true,
          text: "Pwf (Presión de fondo fluyente)",
        },
      },
    },
  };
  var myChart1 = new Chart(chartContext1, {
    type: "line",
    data: initialData,
    options: chartOptions,
  });
  var myChart2 = new Chart(chartContext2, {
    type: "line",
    data: initialData,
    options: chartOptions,
  });
  var myChartModal1 = new Chart(chartContextModal1, {
    type: "line",
    data: initialData,
    options: chartOptions,
  });
  var myChartModal2 = new Chart(chartContextModal2, {
    type: "line",
    data: initialData,
    options: chartOptions,
  });
  // Agregar evento al botón para actualizar el gráfico
  const boton = document.getElementById("calcular");
  boton.addEventListener("click", function () {
    var dataEnv = {
      qo: document.getElementById("qo").value,
      prP: document.getElementById("prP").value,
      pwfP: document.getElementById("pwfP").value,
      pwfF: document.getElementById("pwfF").value,
      prF: document.getElementById("prF").value,
      n: document.getElementById("n").value,
    };
    $.ajax({
      type: "POST",
      url: "/productividad/eickmeier",
      data: JSON.stringify(dataEnv),
      contentType: "application/json",
      dataType: "JSON",
      success: done,
      error: errorGraphic,
    });
  });
  function done(result) {
    console.log(result);
    imprimirResultados(result);
    const newData1 = {
      labels: result.lqoP,
      datasets: [
        {
          label: "Vogel",
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 1,
          data: result.lpwfP,
          fill: false,
          tension: 1,
        },
      ],
    };
    const newData2 = {
      labels: result.lqoF,
      datasets: [
        {
          label: "Vogel",
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 1,
          data: result.lpwfF,
          fill: false,
          tension: 1,
        },
      ],
    };
    // Actualizar el gráfico con los nuevos datos
    myChart1.data = newData1;
    myChart1.update();
    myChart2.data = newData2;
    myChart2.update();
    myChartModal1.data = newData1;
    myChartModal1.update();
    myChartModal2.data = newData2;
    myChartModal2.update();
  }
  function errorGraphic(error) {
    alert(error.message);
  }

  //Imprimir resultados
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
