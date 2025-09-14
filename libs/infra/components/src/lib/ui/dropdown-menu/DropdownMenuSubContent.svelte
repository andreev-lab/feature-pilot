<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: DropdownMenuPrimitive.SubContentProps = $props();
</script>

<style lang="scss">
    :global([data-slot="dropdown-menu-sub-content"]) {
        background-color: var(--popover);
        color: var(--popover-foreground);
        z-index: 50;
        min-width: 8rem;
        overflow: hidden;
        border-radius: 0.375rem;
        border: 1px solid var(--border);
        padding: 0.25rem;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        transform-origin: var(--bits-dropdown-menu-content-transform-origin);
    }
</style>

<DropdownMenuPrimitive.SubContent
	bind:ref
	data-slot="dropdown-menu-sub-content"
	class={className}
	{...restProps}
/>