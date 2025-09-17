<script lang="ts">
  import type { DropdownMenuContentProps, DropdownMenuPortalProps } from 'bits-ui';
  import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
    class: className,
		sideOffset = 4,
		portalProps,
		...restProps
	}: DropdownMenuContentProps & {
    class?: string;
		portalProps?: DropdownMenuPortalProps;
	} = $props();
</script>

<style lang="scss">
  :global(.dropdown-menu-content) {
    background-color: var(--popover);
    color: var(--popover-foreground);
    z-index: 50;
    min-width: 8rem;
    overflow-y: auto;
    overflow-x: hidden;
    border-radius: 0.375rem;
    border: 1px solid var(--border);
    padding: 0.25rem;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    outline: none;
    max-height: var(--bits-dropdown-menu-content-available-height);
    transform-origin: var(--bits-dropdown-menu-content-transform-origin);
  }
</style>

<DropdownMenuPrimitive.Portal {...portalProps}>
	<DropdownMenuPrimitive.Content
		bind:ref
		class={clsx("dropdown-menu-content", className)}
		{sideOffset}
		{...restProps}
	/>
</DropdownMenuPrimitive.Portal>
