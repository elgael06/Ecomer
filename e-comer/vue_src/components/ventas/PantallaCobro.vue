
<template>
  <div class="modal_base" id="modal_cobro">
    <div class="card">
      <div class="card-header efecto bg-success text-white">
        <i class="fa fa-close close" @click="cerrar"></i>
        <label>Detalle De Cobro</label>
      </div>
      <div class="card-body">
        <label>Resumen</label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PantallaCobro",
  methods: {
    cerrar() {
      document.querySelector("#modal_cobro").style.display = "none";
    }
  }
};
</script>


