<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";
	import type { ComponentProps } from "svelte";

	let {
		ref = $bindable(null),
		inset,
		...restProps
	}: ComponentProps<typeof MenubarPrimitive.GroupHeading> & {
		inset?: boolean;
	} = $props();
</script>

<MenubarPrimitive.GroupHeading
	bind:ref
	data-slot="menubar-group-heading"
	data-inset={inset}
	{...restProps}
/>

<style lang="scss">
    [data-slot="menubar-group-heading"] {
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;

        &[data-inset] {
            padding-left: 2rem;
        }
    }
</style>