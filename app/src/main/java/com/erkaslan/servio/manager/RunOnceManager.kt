package com.erkaslan.servio.manager

import android.content.Context
import android.content.SharedPreferences
import android.util.Log
import android.widget.Toast
import com.erkaslan.servio.model.RetrofitClient
import com.erkaslan.servio.model.Token
import com.erkaslan.servio.model.UserService
import com.erkaslan.servio.model.User
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import com.google.gson.Gson





class RunOnceManager () {
    lateinit var userService: UserService
    lateinit var userList: MutableList<User>

    fun runOnce(context: Context){
        val service = RetrofitClient.getClient().create(UserService::class.java)
        var sharedPreferences: SharedPreferences.Editor? = context.getSharedPreferences("app", Context.MODE_PRIVATE)?.edit()

        authenticate(context, sharedPreferences, service)

    }

    private fun authenticate(context: Context, sharedPreferences: SharedPreferences.Editor?, service: UserService){

        //Check authentication
        val token: String? = context.getSharedPreferences("app", Context.MODE_PRIVATE).getString("token", "null")
        val username: String? = context.getSharedPreferences("app", Context.MODE_PRIVATE).getString("username", "null")
        if(token.equals("null") || token.isNullOrEmpty() || username.equals("null") || username.isNullOrEmpty()){
            sharedPreferences?.putBoolean("isLoggedIn", false)
            sharedPreferences?.commit()
        }else{
            Log.d("EX", token)
            Log.d("EX", username)
            val check = service.loginCheck("Token " + token, username)

            check.enqueue(object : Callback<User> {
                override fun onResponse(call: Call<User>, response: Response<User>) {
                    Log.d("EX", response.body().toString())
                    if (response.isSuccessful) {
                        Toast.makeText(context, "User is logged in as user: " + response.body()?.pk.toString() , Toast.LENGTH_LONG).show()
                        sharedPreferences?.putBoolean("isLoggedIn", true)
                        val user = response.body() as User
                        val gson = Gson()
                        val json = gson.toJson(user)
                        sharedPreferences?.putString("currentUser", json)
                        sharedPreferences?.commit()
                    } else if (response.code() == 400) {
                        Log.d("EX",response.errorBody().toString())
                    }
                    else if (response.code() == 301){
                        sharedPreferences?.putBoolean("isLoggedIn", false)
                        sharedPreferences?.commit()
                        Log.d("EX", "Not Successfull")
                    }
                }

                override fun onFailure(call: Call<User>, t: Throwable) {
                    Log.d("EX", "Failed: " + t.toString())
                }
            })
        }

    }
}