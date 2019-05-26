/***
 * Crear Modificar Ordenes De Compras
 */


 Vue.component('producto-lista',{
     props:['producto','eliminar'],
     template:`
        <div class="panel panel-info">
            <div class="panel-heading">
                <i class="fa fa-close" style="float:right" @click="eliminar(producto)"></i>
                <label>ID: {{producto.id}}</label>
                <label> {{producto.descripcion}}</label>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-sm-2"  style="max-width:160px;display:inline-block">
                        <label>cantidad</label>
                        <input type="text" @keypress="on_cantidad" v-model="producto.cantidad" class="form-control" />
                    </div>
                    <div class="col-sm-2" style="max-width:160px;display:inline-block">
                        <label>costo</label>
                        <input type="text"@keypress="on_costo" v-model="producto.costo" class="form-control" />
                    </div>
                    <div class="col-sm-2" style="max-width:160px;display:inline-block">
                        <label>iva</label>
                        <input type="text" v-model="producto.iva" class="form-control" />
                    </div>
                    <div class="col-sm-2" style="max-width:160px;display:inline-block">
                        <label>margen</label>
                        <input type="text" disabled v-model="producto.margen" class="form-control" />
                    </div>
                    <div class="col-sm-2" style="max-width:160px;display:inline-block">
                        <label>venta</label>
                        <input type="text" disabled v-model="producto.venta" class="form-control" />
                    </div>
                    <div class="col-sm-2" style="max-width:160px;display:inline-block">
                        <label>total</label>
                        <input type="text" disabled v-model="producto.total" class="form-control" />
                    </div>
                </div>
            </div>
        </div>
     `,
    methods: {
        on_cantidad(){
            let {cantidad,costo} =this.producto;
            this.producto.total = cantidad* costo;
        },
        on_costo(){
            let {cantidad,costo} =this.producto;
            this.producto.total = cantidad* costo;
        },
    },
 });

Vue.component('modal-orden',{
    props:['orden','productos','lista_proveedores'],
    template:`
        <div class="modal_base" id="moda_orden">
            <div  :class="tipo_modal">
                <div class="panel-heading">
                    <i class="fa fa-close" style="float:right" @click="cerrar"></i>
                    <label>
                        <span v-if="orden.id>0">Editar : orden.id </span>
                        <span v-else>Nueva</span>
                        Orden Compra
                    </label>
                </div>
                <div class="panel-body">
                    <div class="row">
                            <div class="col-sm-4">
                                <label>Proveedor</label>
                                <select class="form-control"  v-model="orden.proveedor" @change="on_proveedor">
                                        <option v-for="item in lista_proveedores" :key="item.Id">{{item.Nombre}}</option>
                                </select>
                            </div>
                            <div class="col-sm-6">
                                <label>Descripcion</label>
                                <input type="text" class="form-control" v-model="orden.Descripcion" />
                            </div>
                            <div class="col-sm-2">
                                <label>Estatus</label>
                                <select class="form-control"  v-model="orden.estatus">
                                        <option value="V">Vigente</option>
                                        <option value="C">Cancelada</option>
                                        <option value="F">Finalizo</option>
                                </select>
                            </div>
                            <div class="col-sm-2" style="max-width:160px;display:inline-block">
                                <label>Productos</label>
                                <input type="text" class="form-control" disabled v-model="orden.productos" />
                            </div>
                            <div class="col-sm-2"  style="max-width:160px;display:inline-block">
                                <label>Total $</label>
                                <input type="text" class="form-control" disabled v-model="orden.Total" />
                            </div>
                            <form class="col-sm-3"  style="max-width:210px;display:inline-block" @submit.prevent="Agregar_producto">
                                <label>Agregar</label>
                                <input type="text" class="form-control" v-model="seleccion.id" />
                            </form>                             
                            <div class="col-sm-5">      
                            <i class="btn btn-info fa fa-search" style="margin-top:20px" > Buscar</i>
                                <i class="btn btn-success fa fa-save" style="margin-top:20px" > Guardar</i>
                                <i class="btn btn-danger fa fa-close" style="float:right;margin-top:20px" > Cancelar</i>
                            </div>
                    </div>
                </div>
                <div class="panel-body">
                    <label>Productos</label>
                    <div style="height:320px;overflow:auto">
                            <producto-lista v-for="item in productos"  v-bind:producto="item" v-bind:eliminar="eliminar"  />
                    </div>
                </div>
            </div>
        </div>
    `,
    data() {
        return {
            seleccion:{
                id:'',
            },
        }
    },  
    updated() {
       
    },
    methods: {
        Agregar_producto(){
            console.log("Agregar : ",this.seleccion.id);
            this.buscar_producto();
        },
        on_proveedor(){
            let index = this.lista_proveedores.findIndex(e=>e.Nombre == this.orden.proveedor)
            console.log(this.orden.proveedor);
            console.log(index)
            if(index>-1){
                this.orden.Folio_proveedor = this.lista_proveedores[index].Id;
            }
        },
        cerrar(){
            
            document.querySelector("#moda_orden").style.display="none";
        },
        eliminar(seleccion){
            if(confirm(`Eliminar el Producto ${seleccion.descripcion} ?`)){
                let indice = this.productos.findIndex(e=>e.id == seleccion.id)
                this.productos.splice(indice,1);
            }
        },
        actualizar_datos(){
            let total = 0;
            this.orden.productos = this.productos.length || 0;
            
            for(p of  this.productos){
                total+= p.total;
            }
            this.orden.Total = total;
        },
        buscar_producto(){
            document.querySelector("#modal_load").style.display="flex";
            fetch(`productos/api?id=${this.seleccion.id}`, {
                method: 'get',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .catch(err =>{
                     console.error("Error=>", err);
                     alert("Codigo No Relacionado A producto !!!")
                     document.querySelector("#modal_load").style.display="none";
                 })
                .then(res => res.json()
                    .then(respuesta => {
                    if( respuesta.producto.id){
                            let index = this.productos.findIndex(e=>e.id== respuesta.producto.id);
                            if(index ===-1)
                                this.productos.push(respuesta.producto);
                            else{
                            let  prod =  this.productos.filter(e=>e.id== respuesta.producto.id);
                            for(p of prod){
                                p.cantidad += respuesta.producto.cantidad;
                                p.total += respuesta.producto.total;
                            }
                            }
                            this.actualizar_datos();
                        }
                        else 
                        alert(`Codigo : ${this.seleccion.id}\n No Relacionado A producto !!!`)
                    document.querySelector("#modal_load").style.display="none";                    
                    this.seleccion.id ='';
                    }).catch(e=>{
                        console.error("Error=>", e);
                        alert("Codigo No Relacionado A producto !!!")
                        document.querySelector("#modal_load").style.display="none";
                    })
                );
        }
    },
    computed: {
        tipo_modal(){
            return this.orden.id>0?"panel panel-primary animate":"panel panel-default animate";
        },
    },
});
 
let root = new Vue({
    el:'#root',
    data() {
        return {
            orden:{
                'id':0,
            'Folio_proveedor':0,
            'proveedor':'',
            'productos':0,
            'Total':0.0,
            'Descripcion':'',
            'estatus':'V',
            },
            productos:[],
            lista_ordenes:[],
            lista_proveedores:[],
        }
    },
    created() {
        console.log("Incia...");
    },
    methods: {
        on_nueva(){
            this.orden = {
                'id':0,
            'Folio_proveedor':0,
            'proveedor':'',
            'productos':0,
            'Total':0.0,
            'Descripcion':'',
            'estatus':'V',
            };
            this.productos =[];
            this.obtener_proveedores();
            document.querySelector("#moda_orden").style.display="flex";
        },
        obtener_proveedores(){
            document.querySelector("#modal_load").style.display="flex";
            fetch(`proveedores/api`, {
                method: 'get',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .catch(err => console.error("Error=>", err))
                .then(res => res.json().then(respuesta => {
                    this.lista_proveedores = respuesta.Lista
                    document.querySelector("#modal_load").style.display="none";
                }));
        },
        Guardar_productos(){
            document.querySelector("#modal_load").style.display="flex";
            fetch(`productos/api`, {
                method: 'post',
                credentials: 'same-origin',
                body:JSON.stringify({
                    id_orden:this.orden.id,
                    productos: this.productos,
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .catch(err => console.error("Error=>", err))
                .then(res => res.json().then(respuesta => {
                  alert(respuesta.Productos)
                    document.querySelector("#modal_load").style.display="none";
                }));
        }
    },
});