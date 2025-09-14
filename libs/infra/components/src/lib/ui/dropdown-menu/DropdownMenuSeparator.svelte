<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: DropdownMenuPrimitive.SeparatorProps = $props();
</script>

<style lang="scss">
    :global([data-slot="dropdown-menu-separator"]) {
        background-color: var(--border);
        margin: 0.25rem -0.25rem;
        height: 1px;
    }
</style>

<DropdownMenuPrimitive.Separator
	bind:ref
	data-slot="dropdown-menu-separator"
	class={className}
	{...restProps}
/>