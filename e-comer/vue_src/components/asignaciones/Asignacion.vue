<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div class="col-sm-2">
          <label>ID Asignacion:</label>
          <span>{{asignacion.id}}</span>
        </div>
        <div class="col-sm-8">
          <label>Cajer@:</label>
          <i>{{asignacion.usuario}}</i>
        </div>
      </div>
    </div>
    <div class="card-body">
      <div class="row">
        <div class="col-sm-6">
          <label>Asigno:</label>
          <i class="form-control">{{asignacion.usuario_creo}}</i>
        </div>
        <div class="col-sm-6">
          <label>Modifico:</label>
          <i class="form-control">{{asignacion.usuario_modifico}}</i>
        </div>
        <div class="col-sm-3">
          <label>Fondo Caja:</label>
          <i class="form-control">{{asignacion.fondo_caja}}</i>
        </div>
        <div class="col-sm-3">
          <label>Venta Caja:</label>
          <i class="form-control">{{asignacion.fondo_caja}}</i>
        </div>
        <div class="col-sm-3">
          <label>Corte Caja:</label>
          <i class="form-control">{{asignacion.fondo_caja}}</i>
        </div>
        <div class="col-sm-3">
          <label>Diferencia Caja:</label>
          <i class="form-control">{{asignacion.fondo_caja}}</i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Asignacion",
  props: ["asignacion"]
};
</script>

