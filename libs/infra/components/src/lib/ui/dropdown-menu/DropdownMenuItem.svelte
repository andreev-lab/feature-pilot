<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		class: className,
		inset,
		variant = "default",
		...restProps
	}: DropdownMenuPrimitive.ItemProps & {
		inset?: boolean;
		variant?: "default" | "destructive";
	} = $props();
</script>

<style lang="scss">
  :global(.dropdown-menu-item) {
    position: relative;
    display: flex;
    cursor: pointer;
    user-select: none;
    align-items: center;
    gap: 0.5rem;
    border-radius: 0.125rem;
    padding: 0.375rem 0.5rem;
    font-size: 0.875rem;
    outline: none;

    &.inset-* {
      padding-left: 2rem;
    }

    &[data-disabled] {
      pointer-events: none;
      opacity: 0.5;
    }

    &:hover {
      background-color: var(--accent);
      color: var(--accent-foreground);
    }

    &.variant-destructive {
      color: var(--destructive);

      &[data-highlighted] {
        background-color: hsl(var(--destructive) / 0.1);
        color: var(--destructive);
      }
    }

    .dark &[data-variant="destructive"][data-highlighted] {
        background-color: hsl(var(--destructive) / 0.2);
    }

    svg:not([class*='text-']) {
      color: var(--muted-foreground);
    }

    svg:not([class*='size-']) {
      width: 1rem;
      height: 1rem;
    }
    svg {
      pointer-events: none;
      flex-shrink: 0;
    }
  }
</style>

<DropdownMenuPrimitive.Item
	bind:ref
	data-slot="dropdown-menu-item"
	data-inset={inset}
	data-variant={variant}
	class={clsx(
    className,
    'dropdown-menu-item',
    `variant-${variant}`,
    inset && `inset-${inset}`
  )}
	{...restProps}
/>
