<script lang="ts">
  import projector_logo from "$lib/assets/projector_logo.jpg";

  let {children} = $props();
</script>
<div class="bg-muted flex min-h-svh flex-col items-center justify-center gap-6 p-6 md:p-10">
  <div class="flex w-full max-w-sm flex-col gap-6">
    <a href="/" class="flex items-center gap-2 self-center font-medium">
      <div
        class="flex size-12 items-center justify-center"
      >
        <img src={projector_logo} alt="ProjectOR Logo" class="size-12 rounded-md"/>
      </div>
      ProjectOR
    </a>
    {@render children()}
  </div>
</div>