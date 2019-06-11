<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div class="col-sm-12">
          <label>Asignacion</label>
        </div>
        <div class="col-sm-4">
          <label>Fecha</label>
          <input type="date" class="form-control">
        </div>
        <div class="col-sm-4">
          <label>Estatus</label>
          <select class="form-control">
            <option>Vigente</option>
            <option>Finalizado</option>
          </select>
        </div>
        <div class="col-sm-4 mt-4">
          <i class="btn btn-success btn-block fa fa-download">Cargar</i>
        </div>
      </div>
    </div>
    <div class="card-body">
      <label>Liista Asignaciones</label>
      <div style="height:400px">
        <Asignacion v-for="item in listaAsignacion" :key="item"/>
      </div>
    </div>
  </div>
</template>
<<script>
import  Asignacion from './Asignacion';

export default {
    
    components:{
        Asignacion,
    },
    data() {
        return {
            listaAsignacion:[1,2,3,4]
        }
    },
}
</script>