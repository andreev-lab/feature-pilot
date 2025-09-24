<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
	import type { ComponentProps } from "svelte";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		class: className,
		inset,
		...restProps
	}: ComponentProps<typeof DropdownMenuPrimitive.GroupHeading> & {
		inset?: boolean;
	} = $props();
</script>

<style lang="scss">
    :global(.dropdown-menu-group-heading) {
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        font-weight: 600;

        &.inset {
            padding-left: 2rem;
        }
    }
</style>

<DropdownMenuPrimitive.GroupHeading
	bind:ref
	class={clsx("dropdown-menu-group-heading", inset && "inset", className)}
	{...restProps}
/>