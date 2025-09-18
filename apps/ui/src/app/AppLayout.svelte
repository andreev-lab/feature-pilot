<script lang="ts">
  import { Layout, Sidebar } from '@fp/layout';
  import { GitRouting } from '@fp/git/ui';
</script>

<Layout>
  <GitRouting/>
  {#snippet sidebar()}
    <Sidebar/>
  {/snippet}
</Layout>
