<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";
	import CheckIcon from "@lucide/svelte/icons/check";
	import MinusIcon from "@lucide/svelte/icons/minus";
	import type { WithoutChildrenOrChild } from "@fp/infra-components/lib/utils.js";
	import type { Snippet } from "svelte";

	let {
		ref = $bindable(null),
		checked = $bindable(false),
		indeterminate = $bindable(false),
		children: childrenProp,
		...restProps
	}: WithoutChildrenOrChild<MenubarPrimitive.CheckboxItemProps> & {
		children?: Snippet;
	} = $props();
</script>

<MenubarPrimitive.CheckboxItem
	bind:ref
	bind:checked
	bind:indeterminate
	data-slot="menubar-checkbox-item"
	{...restProps}
>
	{#snippet children({ checked, indeterminate })}
		<span class="indicator">
			{#if indeterminate}
				<MinusIcon />
			{:else}
				<CheckIcon class={!checked ? "unchecked" : ""} />
			{/if}
		</span>
		{@render childrenProp?.()}
	{/snippet}
</MenubarPrimitive.CheckboxItem>

<style lang="scss">
  [data-slot="menubar-checkbox-item"] {
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
        width: 1rem;
        height: 1rem;
    }
  }

  .unchecked {
      color: transparent;
  }
</style>