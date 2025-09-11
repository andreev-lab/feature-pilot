<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		...restProps
	}: MenubarPrimitive.SubContentProps = $props();
</script>

<MenubarPrimitive.SubContent
	bind:ref
	data-slot="menubar-sub-content"
	{...restProps}
/>
<style lang="scss">
  @keyframes menubar-in {
    from {
      opacity: 0;
      transform: scale(0.95) var(--slide-from, "");
    }
    to {
      opacity: 1;
      transform: scale(1) translateY(0);
    }
  }

  @keyframes menubar-out {
    from {
      opacity: 1;
      transform: scale(1) translateY(0);
    }
    to {
      opacity: 0;
      transform: scale(0.95) var(--slide-from, "");
    }
  }
  [data-slot="menubar-sub-content"] {
    background-color: var(--popover);
    color: var(--popover-foreground);
    z-index: 50;
    min-width: 8rem;
    overflow: hidden;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    padding: 0.25rem;
    box-shadow: var(--shadow-lg);
    transform-origin: var(--bits-menubar-content-transform-origin);

    &[data-state="open"] {
      animation: menubar-in 0.1s ease-out;
    }
    &[data-state="closed"] {
      animation: menubar-out 0.1s ease-in;
    }
    &[data-side="bottom"] {
        --slide-from: translateY(-0.5rem);
    }
    &[data-side="top"] {
        --slide-from: translateY(0.5rem);
    }
    &[data-side="left"] {
        --slide-from: translateX(0.5rem);
    }
    &[data-side="right"] {
        --slide-from: translateX(-0.5rem);
    }
  }
</style>