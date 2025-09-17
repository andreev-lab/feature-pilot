<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: DropdownMenuPrimitive.SubContentProps = $props();
</script>

<style lang="scss">
  :global(.dropdown-menu-sub-content) {
    background-color: var(--popover);
    opacity: 1;
    color: var(--popover-foreground);
    z-index: 50;
    min-width: 8rem;
    overflow: hidden;
    border-radius: 0.375rem;
    border: 1px solid var(--border);
    padding: 0.25rem;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    transform-origin: var(--bits-dropdown-menu-content-transform-origin);
  }
</style>

<DropdownMenuPrimitive.SubContent
	bind:ref
	class={clsx("dropdown-menu-sub-content", className)}
	{...restProps}
/>
