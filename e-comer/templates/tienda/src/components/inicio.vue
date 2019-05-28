

<template>
        <div>
            <h5 >Contador</h5>
            <i class="btn btn-info  fa fa-plus" @click="sumar">+</i>
            <i class="btn btn-danger fa fa-minus" @click="restar">-</i>

            <p class="numeroro_grande">
                    {{cantidad}}
            </p>
        </div>
</template>

<script>
export default {
    name:"contador",
    data() {
        return {
            cantidad:0,
        }
    },
    methods: {
        sumar(){
                this.cantidad += 1;
        },
        restar(){

            this.cantidad -= this.cantidad>0 ? 1 : (function(){
                alert("no Puede disminuir De \"0\" !!!")
                return 0
            }());
        },
    },
}
</script>

