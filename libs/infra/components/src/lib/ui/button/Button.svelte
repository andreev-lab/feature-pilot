<script lang="ts">
	import type { ButtonProps } from "./types";

	let {
		class: className,
		variant = 'default',
		size = 'default',
		ref = $bindable(null),
		href = undefined,
		type = 'button',
		disabled,
		children,
		...restProps
	}: ButtonProps = $props();

  let hasSvg = false;

  $effect(() => {
    if (ref) {
      hasSvg = !!ref.querySelector('svg');
    }
  });
</script>

<style lang="scss">
  .button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    line-height: 1.25rem;
    font-weight: 500;
    outline: none;
    transition: all 0.2s ease-in-out;
    gap: 0.5rem;
    flex-shrink: 0;

    &:focus-visible {
      outline: 3px solid var(--ring);
      outline-offset: 1px;
    }

    &[aria-invalid="true"] {
      outline: 1px solid var(--destructive);
    }

    &:disabled,
    &[aria-disabled="true"] {
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

    &.button--default {
      background-color: var(--primary);
      color: var(--primary-foreground);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      &:hover {
        background-color: var(--primary);
        opacity: 0.9;
      }
    }

    &.button--destructive {
      background-color: var(--destructive);
      color: var(--destructive-foreground);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      &:hover {
        background-color: var(--destructive);
        opacity: 0.9;
      }
    }

    &.button--outline {
      background-color: transparent;
      border: 1px solid var(--border);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      &:hover {
        background-color: var(--accent);
        color: var(--accent-foreground);
      }
    }
    &.button--secondary {
      background-color: var(--secondary);
      color: var(--secondary-foreground);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      &:hover {
        background-color: var(--secondary);
        opacity: 0.8;
      }
    }

    &.button--ghost {
      &:hover {
        background-color: var(--accent);
        color: var(--accent-foreground);
      }
    }

    &.button--link {
      color: var(--primary);
      text-underline-offset: 4px;
      &:hover {
        text-decoration: underline;
      }
    }

    &.button--default {
      height: 2.25rem;
      padding-left: 1rem;
      padding-right: 1rem;
      padding-top: 0.5rem;
      padding-bottom: 0.5rem;
      &.has-svg {
        padding-left: 0.75rem;
        padding-right: 0.75rem;
      }
    }

    &.button--sm {
      height: 2rem;
      border-radius: 0.375rem;
      padding-left: 0.75rem;
      padding-right: 0.75rem;
      gap: 0.375rem;
      &.has-svg {
        padding-left: 0.625rem;
        padding-right: 0.625rem;
      }
    }

    &.button--lg {
      height: 2.5rem;
      border-radius: 0.375rem;
      padding-left: 1.5rem;
      padding-right: 1.5rem;
      &.has-svg {
        padding-left: 1rem;
        padding-right: 1rem;
      }
    }

    &.button--icon {
      width: 2.25rem;
      height: 2.25rem;
    }
  }
</style>

{#if href}
	<a
		bind:this={ref}
		data-slot="button"
		class="button button--{variant} button--{size} {className || ''} {hasSvg ? 'has-svg' : ''}"
		href={disabled ? undefined : href}
		aria-disabled={disabled}
		role={disabled ? 'link' : undefined}
		tabindex={disabled ? -1 : undefined}
		{...restProps}
	>
		{@render children?.()}
	</a>
{:else}
	<button
		bind:this={ref}
		data-slot="button"
		class="button button--{variant} button--{size} {className || ''} {hasSvg ? 'has-svg' : ''}"
		{type}
		{disabled}
		{...restProps}
	>
		{@render children?.()}
	</button>
{/if}
