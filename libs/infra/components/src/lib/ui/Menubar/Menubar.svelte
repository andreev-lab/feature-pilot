<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		...restProps
	}: MenubarPrimitive.RootProps = $props();
</script>

<MenubarPrimitive.Root
	bind:ref
	data-slot="menubar"
	{...restProps}
/>

<style lang="scss">
  [data-slot="menubar"] {
    background-color: var(--background);
    box-shadow: var(--shadow-xs);
    display: flex;
    height: 2.25rem;
    align-items: center;
    gap: 0.25rem;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    padding: 0.25rem;
  }
</style>