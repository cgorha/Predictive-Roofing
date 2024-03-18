<template>
    <div class="page-add-lead">
      <div class="columns">
          <div class="column is-4 is-offset-4">

              <form @submit.prevent="submitForm">
                  <div class="field">
                      <label>Name</label>
                      <div class="control">
                          <input type="text" class="input" v-model="name">
                      </div>
                  </div>
                  <div class="field">
                      <label>Email</label>
                      <div class="control">
                          <input type="email" class="input" v-model="email">
                      </div>
                  </div>
                  <div class="phoneNumber">
                        <label>Phone Number</label>
                        <div class="control">
                            <input type="text" class="input" v-model="phoneNumber">
                        </div>
                  </div>

                  <div class="field">
                      <label>Address</label>
                      <div class="control">
                          <input type="text" class="input" v-model="address">
                      </div>
                  </div>

                  <div class="field">
                      <label>Damage</label>
                      <div class="control">
                          <input type="text" class="input" v-model="damage">
                      </div>
                  </div>

                  <div class="field">
                      <label>Images</label>
                      <div class="control">
                          <input type="file" class="input" @change="imageUpload">
                      </div>
                  </div>

                  <div class="field">
                      <label>Description</label>
                      <div class="control">
                          <textarea class="textarea" v-model="description" placeholder="Enter description"></textarea>
                      </div>
                  </div>


                  <div class="field">
                      <div class="control">
                          <button class="button is-dark">Add Lead</button>
                      </div>
                  </div>

                  <hr>
              </form>
          </div>
      </div>
  </div>
</template>
<script>

</script>
<style>

    .page-add-lead{
        padding: 30px;
    }

    .textarea {
      width: 100%; /* Adjust width as needed */
      height: 200px; /* Adjust height as needed */
      resize: vertical; /* Allows vertical resizing */
    }




</style>