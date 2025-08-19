<script lang="ts">
  let count = $state(0);
  const increment = () => {
    count += 1;
  };
</script>

<main>
  <button on:click={increment}>
    count is {count}
  </button>
</main>

<style lang="scss">
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
  }
  button {
    padding: 1.5em 3em;
    font-size: 1.2rem;
    color: white;
    background-color: #4CAF50; /* A nice green */
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);

    &:hover {
      background-color: #45a049;
    }
  }
</style>

