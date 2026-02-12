document.addEventListener("DOMContentLoaded", function () {
  const expenseChartElement = document.getElementById("expenseChart");
  if (expenseChartElement) {
    // The replace function is needed because Django templates output single quotes for strings,
    // but JSON.parse requires double quotes.
    const labels = JSON.parse(
      expenseChartElement.dataset.labels.replace(/'/g, '"'),
    );
    const data = JSON.parse(expenseChartElement.dataset.data);

    new Chart(expenseChartElement.getContext("2d"), {
      type: "doughnut",
      data: {
        labels: labels,
        datasets: [
          {
            data: data,
            backgroundColor: [
              "#3B82F6",
              "#10B981",
              "#F59E0B",
              "#EF4444",
              "#8B5CF6",
              "#EC4899",
              "#6366F1",
            ],
            borderWidth: 0,
            hoverOffset: 4,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "right",
          },
        },
      },
    });
  }
});
