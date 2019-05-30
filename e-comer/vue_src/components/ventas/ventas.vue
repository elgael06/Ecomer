<template>
<div class="panel panel-default">
    <div class="panel-heading">
        <strong>{{title}}</strong>
    </div>
    <div class="panel-body">
        <Caja />
        <Asignacion />
    </div>
</div>
</template>

<script>
import Caja from './caja';
import Asignacion from './asignacion'
  export default {
    components:{
      Caja,
      Asignacion,
    },
    data() {
      return {
        title: 'Ventas',

      }
    }
  }
</script>