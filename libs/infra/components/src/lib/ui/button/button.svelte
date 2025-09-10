<script lang="ts">
	import type { HTMLAnchorAttributes, HTMLButtonAttributes } from 'svelte/elements';
  import type { WithElementRef } from '../../utils';

	export type ButtonVariant = "default" | "destructive" | "outline" | "secondary" | "ghost" | "link";
	export type ButtonSize = "default" | "sm" | "lg" | "icon";

	export type ButtonProps = WithElementRef<HTMLButtonAttributes> &
		WithElementRef<HTMLAnchorAttributes> & {
			variant?: ButtonVariant;
			size?: ButtonSize;
		};

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

<style lang="scss" src="./button.scss"></style>

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
