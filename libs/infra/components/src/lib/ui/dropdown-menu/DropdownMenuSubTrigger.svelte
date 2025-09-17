<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
	import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";

	let {
		ref = $bindable(null),
		class: className,
		inset,
		children,
		...restProps
	}: DropdownMenuPrimitive.SubTriggerProps & {
		inset?: boolean;
	} = $props();
</script>

<style lang="scss">
    :global([data-slot="dropdown-menu-sub-trigger"]) {
        display: flex;
        cursor: pointer;
        user-select: none;
        align-items: center;
        gap: 0.5rem;
        border-radius: 0.125rem;
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        outline: none;

        &[data-inset] {
            padding-left: 2rem;
        }

        &[data-disabled] {
            pointer-events: none;
            opacity: 0.5;
        }

                &[data-highlighted],
        &[data-state="open"],
        &:hover {
            background-color: var(--accent);
            color: var(--accent-foreground);
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

    .icon-chevron-right {
        margin-left: auto;
        width: 1rem;
        height: 1rem;
    }
</style>

<DropdownMenuPrimitive.SubTrigger
	bind:ref
	data-slot="dropdown-menu-sub-trigger"
	data-inset={inset}
	class={className}
	{...restProps}
>
	{@render children?.()}
	<ChevronRightIcon class="icon-chevron-right" />
</DropdownMenuPrimitive.SubTrigger>