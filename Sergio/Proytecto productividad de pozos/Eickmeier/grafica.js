document.addEventListener('DOMContentLoaded', function () {
    // Leer datos desde el archivo TXT
    fetch('DATOS_PARA_GRAFICAR.txt') //LLAMA EL ARCHIVO EN DONDE SE TIENEN LOS DATOS DE RESPUESTA
      .then(response => response.text())
      .then(data => {
        // Dividir el contenido del archivo en líneas y luego en pares de valores
        var lines = data.trim().split('\n');
        var labels = [];
        var values = [];
  
        lines.forEach(line => {
          var [label, value] = line.split(',');
          labels.push(label.trim());
          values.push(parseFloat(value.trim()));
        });
  
        // Datos del gráfico
        var chartData = {
          labels: labels,
          datasets: [{
            label: 'IPR',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: values
          }]
        };
  
        // Configuración del gráfico
        var chartOptions = {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        };
  
        // Crear el gráfico
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
          type: 'line',
          data: chartData,
          options: chartOptions
        });
      })
      .catch(error => console.error('Error al leer el archivo:', error));
  });
  