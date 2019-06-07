
<template>
  <div class="card-header bg-primary text-white">
    <div class="row">
      <div class="col-sm-2">
        <label>N. Ticket</label>
        <i class="form-control" style="text-align:right">{{datos.ticket}}</i>
      </div>
      <div class="col-sm-4">
        <label>Cliente</label>
        <i class="form-control">{{datos.cliente}}</i>
      </div>
      <div class="col-sm-2" style="text-align:right">
        <label>Cantidad</label>
        <i class="form-control" style="text-align:right">{{datos.cantidad}}</i>
      </div>
      <div class="col-sm-2" style="text-align:right">
        <label>$total</label>
        <i class="form-control" style="text-align:right">
          <Moneda v-bind:cantidad="datos.total"/>
        </i>
      </div>
      <div class="col-sm-2" style="text-align:right">
        <label>$Desc.</label>
        <i class="form-control" style="text-align:right">
          <Moneda v-bind:cantidad="datos.descuento"/>
        </i>
      </div>
      <hr>
      <form class="col-sm-3" @submit.prevent="buscar_producto" style="text-align:right">
        <label>Producto</label>
        <input
          type="text"
          id="entrada_producto"
          style="text-align:right"
          class="form-control"
          v-model="id_producto"
        >
      </form>
      <div class="col-sm-6">
        <label>Acciones</label>
        <i class="btn btn-primary btn-sm fa fa-search" @click="seleccionar_producto">Buscar</i>
        <i class="btn btn-warning btn-sm fa fa-user" @click="seleccinar_cliente">Cliente</i>
        <i class="btn btn-success btn-sm fa fa-money" @click="pagar_cobro">Cobrar</i>
        <i class="btn btn-danger btn-sm fa fa-trash" @click="cancelar_cobro">Cancelar</i>
      </div>
      <div class="col-sm-3" style="text-align:right">
        <label>Fecha</label>
        <input
          type="text"
          class="form-control"
          style="text-align:right"
          v-model="datos.fecha"
          disabled
        >
      </div>
    </div>
  </div>
</template>

<script>
import Moneda from "../ComponentesGlobales/Moneda";

export default {
  name: "ControlesCaja",
  props: ["datos", "agregar_producto"],
  components: {
    Moneda
  },
  data() {
    return {
      id_producto: ""
    };
  },
  methods: {
    buscar_producto() {
      console.log("Buscar...");
      this.id_producto == "" || this.obtener_producto();
    },
    seleccionar_producto() {
      console.log("Seleccionar...");
    },
    seleccinar_cliente() {
      console.log("Cliente...");
    },
    pagar_cobro() {
      console.log("Pagar...");
    },
    cancelar_cobro() {
      console.log("Cancelar Cobro...");
    },
    obtener_producto() {
      fetch(`/Compras/productos/api?id=${this.id_producto}`, {
        method: "get",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json"
        }
      })
        .catch()
        .then(e => {
          e.json().then(res => {
            this.id_producto = "";
            console.log(res);
            this.agregar_producto(res.producto);
          });
        });
    }
  }
};
</script>



