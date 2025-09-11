<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";
	import CircleIcon from "@lucide/svelte/icons/circle";
	import type { WithoutChild } from "@fp/infra-components/lib/utils.js";

	let {
		ref = $bindable(null),
		children: childrenProp,
		...restProps
	}: WithoutChild<MenubarPrimitive.RadioItemProps> = $props();
</script>

<MenubarPrimitive.RadioItem
	bind:ref
	data-slot="menubar-radio-item"
	{...restProps}
>
	{#snippet children({ checked })}
		<span class="indicator">
			{#if checked}
				<CircleIcon />
			{/if}
		</span>
		{@render childrenProp?.({ checked })}
	{/snippet}
</MenubarPrimitive.RadioItem>

<style lang="scss">
    [data-slot="menubar-radio-item"] {
        position: relative;
        display: flex;
        cursor: default;
        user-select: none;
        align-items: center;
        border-radius: var(--radius-xs);
        padding: 0.375rem 0.5rem 0.375rem 2rem;
        font-size: 0.875rem;
        outline: none;
        gap: 0.5rem;

        &:focus {
            background-color: var(--accent);
            color: var(--accent-foreground);
        }

        &[data-disabled] {
            pointer-events: none;
            opacity: 0.5;
        }

        :global(svg:not([class*="size-"])) {
            width: 1rem;
            height: 1rem;
        }
        :global(svg) {
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

        :global(svg) {
            width: 0.5rem;
            height: 0.5rem;
            fill: currentColor;
        }
    }
</style>