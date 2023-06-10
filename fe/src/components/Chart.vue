<template>
  <div>
<!--    <Bar-->
<!--        id="my-chart-id"-->
<!--        :options="chartOptions"-->
<!--        :data="chartData"-->
<!--    />-->
    <iframe title="test" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=f2cf3751-01ee-4b3f-8bab-05902dd75109&autoAuth=true&ctid=4d05a4c9-2f55-4885-93d2-b27bd33fcfb6" frameborder="0" allowFullScreen="true"></iframe>
  </div>
</template>

<script>
// import { Bar } from 'vue-chartjs'
import { Chart as ChartJS,  Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: "ChartJs",
  // components: { Bar },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
}
</script>

<style scoped>

.pane.sections{
  background-color: red;
}
</style>