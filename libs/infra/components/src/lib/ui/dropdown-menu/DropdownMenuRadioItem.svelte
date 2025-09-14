<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
	import CircleIcon from "@lucide/svelte/icons/circle";
	import { type WithoutChild } from "@fp/infra-components/lib/utils.js";

	let {
		ref = $bindable(null),
		class: className,
		children: childrenProp,
		...restProps
	}: WithoutChild<DropdownMenuPrimitive.RadioItemProps> = $props();
</script>

<style lang="scss">
    :global([data-slot="dropdown-menu-radio-item"]) {
        position: relative;
        display: flex;
        cursor: default;
        user-select: none;
        align-items: center;
        gap: 0.5rem;
        border-radius: 0.125rem;
        padding: 0.375rem 0.5rem 0.375rem 2rem;
        font-size: 0.875rem;
        outline: none;

        &:focus {
            background-color: var(--accent);
            color: var(--accent-foreground);
        }

        &[data-disabled] {
            pointer-events: none;
            opacity: 0.5;
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

    .indicator {
        pointer-events: none;
        position: absolute;
        left: 0.5rem;
        display: flex;
        width: 0.875rem;
        height: 0.875rem;
        align-items: center;
        justify-content: center;
    }

    .icon-circle {
        width: 0.5rem;
        height: 0.5rem;
        fill: currentColor;
    }
</style>

<DropdownMenuPrimitive.RadioItem
	bind:ref
	data-slot="dropdown-menu-radio-item"
	class={className}
	{...restProps}
>
	{#snippet children({ checked })}
		<span class="indicator">
			{#if checked}
				<CircleIcon class="icon-circle" />
			{/if}
		</span>
		{@render childrenProp?.({ checked })}
	{/snippet}
</DropdownMenuPrimitive.RadioItem>