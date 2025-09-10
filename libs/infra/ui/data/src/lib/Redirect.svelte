<script lang="ts">
  import { navigate } from "svelte-routing";

  export let to: string = '';
  console.log(`redirect to ${to}`);
  navigate(to, {replace: true})
</script>
