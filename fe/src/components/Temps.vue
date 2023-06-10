<template>
  <div class="box">

    <div class="chart">
      <ChartJs></ChartJs>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ChartJs from "@/components/Chart";
export default {
  name: "TempsHelp",
  components: {ChartJs},
  data () {
    return {
      array: [],
      country: "Country"
    }
  },
  mounted() {
      axios.get("http://127.0.0.1:4012/api/v1/obtener_columna_como_array?country=" + this.country)
          .then(response => {
            this.array = response.data
            console.log(response.data.message)
          })
  }

}
</script>

<style scoped>
.chart {
  width: 50%;
  height: 50%;
}
</style>