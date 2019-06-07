<template>
  <div class="card">
    <ControlesCaja v-bind:datos="cavecera_caja" v-bind:agregar_producto="agregar_producto"/>
    <div class="card-body">
      <label>Lista Productos :</label>
      <div style="height:340px;overflow:auto">
        <table class="table table-condensed">
          <thead>
            <tr class="bg-info text-white">
              <th>Folio</th>
              <th>Descripcion</th>
              <th>Costo</th>
              <th>Cantidad</th>
              <th>Descuento</th>
              <th>Total</th>
              <th>Accion</th>
            </tr>
          </thead>
          <tbody>
            <productoLista
              v-for="(item,index) in productos_lista"
              v-bind:indicadores="indicadores"
              v-bind:item="item"
              v-bind:index="index"
              v-bind:eliminar="eliminar"
              :key="item.folio +'_'+ index"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import ControlesCaja from "./ControlesCaja";
import PrductosCaja from "./ProductosCaja";
import productoLista from "./ProductoLista";

export default {
  name: "Caja",
  components: {
    ControlesCaja,
    PrductosCaja,
    productoLista
  },
  data() {
    return {
      cavecera_caja: {
        ticket: 0,
        id_cliente: 0,
        cliente: "",
        cantidad: 0,
        total: 0,
        descuento: 0,
        fecha: "2019-06-01"
      },
      productos_lista: []
    };
  },
  created() {
    console.log(" Caja...");
  },
  updated() {
    this.indicadores();
  },
  methods: {
    agregar_producto(producto) {
      if (producto.id > 0) {
        let index = this.productos_lista.findIndex(e => e.folio == producto.id);
        if (index == -1) {
          this.productos_lista.push({
            folio: producto.id,
            descripcion: producto.descripcion,
            costo: producto.venta,
            cantidad: producto.cantidad,
            descuento: 0,
            total: producto.venta,
            margen: producto.margen
          });
        } else {
          this.productos_lista[index].cantidad += producto.cantidad;
          this.productos_lista[index].total +=
            producto.venta *
              (1 - this.productos_lista[index].descuento / 100) ||
            producto.venta;
        }
      } else alert("No Se Encuentra el producto !!!");
      this.indicadores();
    },
    eliminar(index) {
      if (confirm("Eliminar ?")) this.productos_lista.splice(index, 1);
    },
    indicadores() {
      this.cavecera_caja.cantidad = this.productos_lista.length;
      this.cavecera_caja.total = 0;
      this.productos_lista.map(e => {
        this.cavecera_caja.total += e.total;
        return e;
      });
      this.cavecera_caja.descuento = 0;
      this.productos_lista.map(e => {
        let total_neto = parseFloat(e.costo) * e.cantidad;
        let descuento = parseFloat(e.descuento / 100);

        this.cavecera_caja.descuento += total_neto * descuento;

        return e;
      });
    }
  },
  computed: {}
};
</script>



