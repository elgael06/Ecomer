<template>
<div class="panel panel-default">  
    <Caja />
    <Asignacion />
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