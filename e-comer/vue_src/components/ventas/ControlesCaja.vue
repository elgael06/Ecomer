
<template>
    <div class="panel-heading">
        <div class="row">
            <div class="col-sm-2">
                <label>N. Ticket</label>
                <i class="form-control">{{datos.ticket}}</i>
            </div>
            <div class="col-sm-4">
                <label>Cliente</label>
                <i class="form-control">{{datos.cliente}}</i>
            </div>
            <div class="col-sm-2">
                <label>Cantidad</label>
                <i class="form-control">{{datos.cantidad}}</i>
            </div>
            <div class="col-sm-2">
                <label>$total</label>
                <i class="form-control">$ {{datos.total}}</i>
            </div>
            <div class="col-sm-2">
                <label>$Desc.</label>
                <i class="form-control">$ {{datos.descuento}}</i>
            </div>
            <hr />
            <form class="col-sm-3" @submit.prevent="buscar_producto">
                <h4>Producto</h4>
                <input type="text" id="entrada_producto" class="form-control" v-model="id_producto" />
            </form>
            <div class="col-sm-6">
                <h4>Acciones</h4>
                <i class="btn btn-default btn-sm fa fa-search" @click="seleccionar_producto"> Buscar</i>
                <i class="btn btn-warning btn-sm fa fa-user" @click="seleccinar_cliente"> Cliente</i>
                <i class="btn btn-success btn-sm fa fa-money" @click="pagar_cobro"> Cobrar</i>
                <i class="btn btn-danger btn-sm fa fa-trash" @click="cancelar_cobro"> Cancelar</i>
            </div>
            <div class="col-sm-3">
                <h4>Fecha</h4>
                <input type="text" class="form-control" v-model="datos.fecha" disabled />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:'ControlesCaja',
    props:['datos','agregar_producto'],
    data() {
        return {
            id_producto:'',
        }
    },
    methods:{
        buscar_producto(){
            console.log("Buscar...");
            this.id_producto=="" || this.obtener_producto();
        },
        seleccionar_producto(){
            console.log("Seleccionar...");            
        },
        seleccinar_cliente(){
            console.log("Cliente...");
        },
        pagar_cobro(){
            console.log("Pagar...");
        },
        cancelar_cobro(){
            console.log("Cancelar Cobro...");
        },
        obtener_producto(){
            fetch(`/Compras/productos/api?id=${this.id_producto}`,{
                 method: 'get',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .catch()
            .then(e=>{
                e.json().then(res=>{
                    this.id_producto ='';
                    console.log(res);
                    this.agregar_producto(res.producto);
                })
            })
        },
    },
}
</script>



