<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: DropdownMenuPrimitive.SeparatorProps = $props();
</script>

<style lang="scss">
    :global(.dropdown-menu-separator) {
        background-color: var(--color-border);
        margin: 0.25rem -0.25rem;
        height: 1px;
    }
</style>

<DropdownMenuPrimitive.Separator
	bind:ref
	class={clsx("dropdown-menu-separator", className)}
	{...restProps}
/>
