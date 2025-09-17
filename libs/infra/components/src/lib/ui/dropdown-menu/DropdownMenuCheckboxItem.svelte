<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
	import CheckIcon from "@lucide/svelte/icons/check";
	import MinusIcon from "@lucide/svelte/icons/minus";
	import { type WithoutChildrenOrChild } from "@fp/infra-components/lib/utils.js";
	import type { Snippet } from "svelte";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		checked = $bindable(false),
		indeterminate = $bindable(false),
		class: className,
		children: childrenProp,
		...restProps
	}: WithoutChildrenOrChild<DropdownMenuPrimitive.CheckboxItemProps> & {
		children?: Snippet;
	} = $props();
</script>

<style lang="scss">
    :global(.dropdown-menu-checkbox-item) {
        position: relative;
        display: flex;
        cursor: pointer;
        user-select: none;
        align-items: center;
        gap: 0.5rem;
        border-radius: 0.125rem;
        padding: 0.375rem 0.5rem 0.375rem 2rem;
        font-size: 0.875rem;
        outline: none;

                &[data-highlighted],
        &:hover {
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

    .icon-minus {
        width: 1rem;
        height: 1rem;
    }

    .icon-check {
        width: 1rem;
        height: 1rem;
        &.transparent {
            color: transparent;
        }
    }
</style>

<DropdownMenuPrimitive.CheckboxItem
	bind:ref
	bind:checked
	bind:indeterminate
	class={clsx("dropdown-menu-checkbox-item", className)}
	{...restProps}
>
	{#snippet children({ checked, indeterminate })}
		<span class="indicator">
			{#if indeterminate}
				<MinusIcon class="icon-minus" />
			{:else}
				<CheckIcon class={[!checked && 'transparent', 'icon-check']} />
			{/if}
		</span>
		{@render childrenProp?.()}
	{/snippet}
</DropdownMenuPrimitive.CheckboxItem>
