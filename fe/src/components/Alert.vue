<template>

  <div class="container">

    <div class="columns is-centered">
      <div class="column is-half">
        <div class="alert m-4 is-align-content-center has-text-centered" :class="alertColor()" @click="toHelp()">
          Proxima fecha para que ocurra un {{disaster}} en {{country}}
          <div>
            {{dateEstimate}}
          </div>
        </div>
      </div>
      <div class="mt-4 column">
        <label for="mensaje">Pais:</label>
        <input type="text" id="mensaje" v-model="country">
        <div>
          <label for="mensaje">Desastre:</label>
          <input type="text" id="mensaje" v-model="disaster">
          <p>{{ texto }}</p>
        </div>
        <button class="button" @click="consultar()">Consultar</button>
      </div>

    </div>

  </div>

</template>

<script>
import router from "@/router";
import axios from 'axios'

export default {
  name: "AlertHelp",
  data() {
    return {
      alert: true,
      country: "Argentina",
      disaster: "Riverine flood",
      dateEstimate: "",
    }
  },
  mounted() {
    this.consultar()
  },
  methods: {
    alertColor() {
      if(this.alert) {
        return 'box has-background-danger'
      } else {
        return 'box has-background-success'
      }
    },
    toHelp() {
      router.push({name: "TipsHelpView"});
    },
    consultar() {
      axios.get(`http://127.0.0.1:4012/api/v1/alert?country=${this.country}&disaster=${this.disaster}`)
          .then(response => {
            const fechaString = response.data;
            const fecha = new Date(fechaString);

            const dia = fecha.getDate();

            const meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
            const mes = meses[fecha.getMonth()];

            const anio = fecha.getFullYear();

            const fechaFormateada = `${dia} de ${mes} de ${anio}`;

            console.log(fechaFormateada);

            console.log(response.data)

            this.dateEstimate = fechaFormateada
          })
          .catch(err => {
            console.log(err)
          })
    }
  },




}
</script>

<style scoped>
.alert {
  width: 50%
}
</style>