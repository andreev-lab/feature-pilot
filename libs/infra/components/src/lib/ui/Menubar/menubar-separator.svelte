<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		...restProps
	}: MenubarPrimitive.SeparatorProps = $props();
</script>

<MenubarPrimitive.Separator
	bind:ref
	data-slot="menubar-separator"
	{...restProps}
/>
<style lang="scss">
    [data-slot="menubar-separator"] {
        background-color: var(--border);
        height: 1px;
        margin: 0.25rem -0.25rem;
    }
</style>